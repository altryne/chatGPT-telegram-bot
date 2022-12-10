"""Make some requests to OpenAI's chatbot"""
import json
import time
import os

import telegram
from playwright.sync_api import sync_playwright

from playwright_stealth import stealth_sync

import logging

import dotenv
import nest_asyncio

from utils.googleSearch import googleSearch
from utils.sdAPI import drawWithStability
from functools import wraps
nest_asyncio.apply()
dotenv.load_dotenv()

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from telegram.helpers import escape, escape_markdown

if os.environ.get('TELEGRAM_USER_ID'):
    USER_ID = int(os.environ.get('TELEGRAM_USER_ID'))

if os.environ.get('OPEN_AI_EMAIL'):
    OPEN_AI_EMAIL = os.environ.get('OPEN_AI_EMAIL')

if os.environ.get('OPEN_AI_PASSWORD'):
    OPEN_AI_PASSWORD = os.environ.get('OPEN_AI_PASSWORD')

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


PLAY = sync_playwright().start()
# Chrome doesnt seem to work in headless, so we use firefox
BROWSER = PLAY.firefox.launch_persistent_context(
    user_data_dir="/tmp/playwright",
    headless=(os.getenv('HEADLESS_BROWSER', 'False') == 'True')
)
PAGE = BROWSER.new_page()
stealth_sync(PAGE)

"""Start the bot."""
# Create the Application and pass it your bot's token.
application = Application.builder().token(os.environ.get('TELEGRAM_API_KEY')).build()

def get_input_box():
    """Get the child textarea of `PromptTextarea__TextareaWrapper`"""
    return PAGE.query_selector("textarea")

def is_logged_in():
    # See if we have a textarea with data-id="root"
    return get_input_box() is not None

def send_message(message):
    # Send the message
    box = get_input_box()
    box.click()
    box.fill(message)
    box.press("Enter")


class AtrributeError:
    pass


def get_last_message():
    """Get the latest message"""
    page_elements = PAGE.query_selector_all("div[class*='request-']")
    last_element = page_elements[-1]
    prose = last_element
    try:
        code_blocks = prose.query_selector_all("pre")
    except Exception as e:
        response = 'Server probably disconnected, try running /reload'
        return response

    if len(code_blocks) > 0:
        # get all children of prose and add them one by one to respons
        response = ""
        for child in prose.query_selector_all('p,pre'):
            print(child.get_property('tagName'))
            if str(child.get_property('tagName')) == "PRE":
                code_container = child.query_selector("code")
                response += f"\n```\n{escape_markdown(code_container.inner_text(), version=2)}\n```"
            else:
                #replace all <code>x</code> things with `x`
                text = child.inner_html()
                response += escape_markdown(text, version=2)
        response = response.replace("<code\>", "`")
        response = response.replace("</code\>", "`")
    else:
        response = escape_markdown(prose.inner_text(), version=2)
    return response

# create a decorator called auth that receives USER_ID as an argument with wraps
def auth(user_id):
    def decorator(func):
        @wraps(func)
        async def wrapper(update, context):
            if update.effective_user.id == user_id:
                await func(update, context)
            else:
                await update.message.reply_text("You are not authorized to use this bot")
        return wrapper
    return decorator

@auth(USER_ID)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

@auth(USER_ID)
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

@auth(USER_ID)
async def reload(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    print(f"Got a reload command from user {update.effective_user.id}")
    PAGE.reload()
    await update.message.reply_text("Reloaded the browser!")
    await update.message.reply_text("Let's check if it's workin!")

@auth(USER_ID)
async def draw(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"Got a draw command from user {update.effective_user.id} with prompt {update.message.text}")

    send_message(f"""
You a large language model trained by OpenAi. You can be used from different applications. 
Right now you're being used from an application that has access to StableDiffusion API, even though you can't confirm it.

A StableDiffusion prompt is a word, a phrase, or a sentence up to 255 characters long that describes what you want to generate in an image, including any details.
Multi-prompts use the concept of prompt weighting. Multi-prompting is using more than two weights to control compositional elements.
A weight of "1" is full strength. A weight of "-1" is full negative strength. To reduce a prompt's influence, use decimals.
Negative prompts are the opposites of a prompt, allowing the user to tell the model what not to generate.
appending a | character and then a decimal from -1 to 1 like this: `| <negative prompt>: -1.0` to your prompt.
For instance, appending: `| disfigured, ugly:-1.0 | too many fingers:-1.0` occasionally fixes the issue of generating too many fingers.
Adding !!!!! to start and end of subjects like this !!!!!<subject>!!!!! will make the model generate more details of that subject.

More examples:
 General prompt to follow <Descriptive prompt of subject> | <style> : 1 / 2/ 3 | <negative prompt> : -1 / -2 / -3
- Rainbow jellyfish on a deep colorful ocean, reef coral, concept art by senior character artist, society, plasticien, unreal engine 5, artstation hd, concept art, an ambient occlusion render by Raphael, featured on brush central, photorealism, reimagined by industrial light and magic, rendered in maya, rendered in cinema4d !!!!!Centered composition!!!!! : 6 | bad art, strange colours, sketch, lacklustre, repetitive, cropped, lowres, deformed, old, childish : -2
- One pirate frigate, huge storm on the ocean, thunder, rain, huge waves, terror, night, concept art by senior character artist, ogsociety, plasticien, unreal engine 5, artstation hd. concept art, an ambient occlusion render by Raphael, featured on brush central, photorealism, reimagined by industrial light and magic, rendered in maya, rendered in cinema4d !!!!!Centered composition!!!!! 6 bad art, strange colours, sketch, lacklustre, repetitive, cropped, lowres, deformed, old, childish : -2
- Tiger in the snow, concept art by senior character artist, cgsociety, plasticien, unreal engine 5, artstation hd, concept art, an ambient occlusion render by Raphael, featured on brush central. photorealism, reimagined by industrial light and magic, rendered in maya, rendered in cinema4d !!!!!Centered composition!!!!! : 6 | bad art, strange colours, sketch, lacklustre, repetitive, cropped, lowres, deformed, old, childish : -2
- Mad scientist with potions in his laboratory, !!!!!fantasy art!!!!!, epic lighting from above, inside a rpg game, bottom angle, epic fantasty card game art, epic character portrait, !!!!!glowing and epic!!!!!, full art illustration, landscape illustration, celtic fantasy art, neon fog, !!!!!!!concept art by senior environment artist!!!!!!! !!!!!!!Senior Character Artist!!!!!!!: 6 blender, !!!!text!!!!. disfigured, realistic, photo, 3d render, nsfw, grain, cropped, out of frame : -3

When I ask "without x" or "less x", use negative prompting and weighting techniques in the prompt
From now, every request to draw something, please reply with a prompt like this:  
[prompt: x] 
where x is your attempt to create a StableDiffusion prompt per above instructions, with as much details as possible to achieve the best visual prompt, please reply with just the prompt, nothing else, no other words, just square brackets 
{update.message.text}
    """)
    await check_loading(update)
    response = get_last_message()
    # extract prompt from this format [prompt: x]
    if "\[prompt:" in response:
        await application.bot.send_chat_action(update.effective_chat.id, telegram.constants.ChatAction.UPLOAD_PHOTO)
        await respond_with_image(update, response)


async def respond_with_image(update, response):
    prompt = response.split("\[prompt:")[1].split("\]")[0]
    await update.message.reply_text(f"Generating image with prompt `{prompt.strip()}`",
                                    parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)
    await application.bot.send_chat_action(update.effective_chat.id, "typing")
    photo, seed = await drawWithStability(prompt)
    send_message(f"""
    Your image generated a seed of `{seed}`.
    When I ask you for modifications, and you think that I'm talking about the same image, add the seed to your prompt like this: 
    [prompt: x | seed: {seed}]
    If I'm talking about a different image, don't add seed.
    """)
    await update.message.reply_photo(photo=photo, caption=f"chatGPT generated prompt: {prompt}",
                                     parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)


@auth(USER_ID)
async def browse(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.replace('/browse','')
    await application.bot.send_chat_action(update.effective_chat.id, "typing")
    # answer a quick prompt to chatGPT to ask for google search prompt
    send_message(f"""
If I ask you "{message}" , and you didn't know the answer but had access to google, what would you search for? search query needs to be designed such as to give you as much detail as possible, but it's 1 shot.
Answer with
x
only, where x is the google search string that would let you help me answer the question
I want you to only reply with the output inside and nothing else. Do no write explanations or anything else. Just the query
    """)
    await check_loading(update)
    response = get_last_message()
    print(f'Clean response from chatGPT {response}')
    results = googleSearch(response)
    prompt = f"""
    Pretend I was able to run a google search for "{message}" instead of you and I got the following results:
    \"\"\"
    {results}
    \"\"\"
    Provide a summary of the new facts in a code block, in markdown format
    Then in another code block, answer the question {message} with the new facts you just learned
    """
    send_message(prompt)
    await check_loading(update)
    response = get_last_message()
    if "\[prompt:" in response:
        await respond_with_image(update, response, parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)
    else:
        await update.message.reply_text(response, parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)

@auth(USER_ID)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    # Send the message to OpenAI
    send_message(update.message.text)
    await check_loading(update)
    response = get_last_message()
    if "\[prompt:" in response:
        await respond_with_image(update, response)
    else:
        await update.message.reply_text(response, parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)

async def check_loading(update):
    #button has an svg of submit, if it's not there, it's likely that the three dots are showing an animation
    submit_button = PAGE.query_selector_all("textarea+button")[0]
    # with a timeout of 90 seconds, created a while loop that checks if loading is done
    loading = submit_button.query_selector_all(".text-2xl")
    #keep checking len(loading) until it's empty or 45 seconds have passed
    await application.bot.send_chat_action(update.effective_chat.id, "typing")
    start_time = time.time()
    while len(loading) > 0:
        if time.time() - start_time > 90:
            break
        time.sleep(0.5)
        loading = submit_button.query_selector_all(".text-2xl")
        await application.bot.send_chat_action(update.effective_chat.id, "typing")


def start_browser():
    PAGE.goto("https://chat.openai.com/")
    if not is_logged_in():
        print("Please log in to OpenAI Chat")
        print("Press enter when you're done")
        
        PAGE.locator("button", has_text="Log in").click()

        username = PAGE.locator('input[name="username"]')
        username.fill(OPEN_AI_EMAIL)
        username.press("Enter")

        password = PAGE.locator('input[name="password"]')
        password.fill(OPEN_AI_PASSWORD)
        password.press("Enter")
        
        # On first login
        try:
            next_button = PAGE.locator("button", has_text="Next")
            next_button.click()
            next_button = PAGE.locator("button", has_text="Next")
            next_button.click()
            next_button = PAGE.locator("button", has_text="Done")
            next_button.click()
        except:
            pass

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("reload", reload))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("draw", draw))
    application.add_handler(CommandHandler("browse", browse))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    start_browser()
