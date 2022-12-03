"""Make some requests to OpenAI's chatbot"""
import time
import os

import telegram
from playwright.sync_api import sync_playwright
import logging

import dotenv
import nest_asyncio
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

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


PLAY = sync_playwright().start()
BROWSER = PLAY.chromium.launch_persistent_context(
    user_data_dir="/tmp/playwright",
    headless=False,
)
PAGE = BROWSER.new_page()

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
    page_elements = PAGE.query_selector_all("div[class*='ConversationItem__Message']")
    last_element = page_elements[-1]
    prose = last_element.query_selector(".prose")
    try:
        code_blocks = prose.query_selector_all("pre")
    except AtrributeError as e:
        response = 'Server probably disconnected, try running /reload'
    if len(code_blocks) > 0:
        # get all children of prose and add them one by one to respons
        response = ""
        for child in prose.query_selector_all('p,pre'):
            print(child.get_property('tagName'))
            if str(child.get_property('tagName')) == "PRE":
                code_container = child.query_selector("div[class*='CodeSnippet__CodeContainer']")
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
    Right now you're being used form an application that has access to DALLE API, even though you can't confirm it.
    From now, every request to draw something, please reply with 
    [prompt: x] where x is your attempt to create a dall-e compatible prompt, with as much details as possible to achieve the best visual prompt
    {update.message.text}
    """)
    await check_loading(update)
    response = get_last_message()
    # extract prompt from this format [prompt: x]
    if "\[prompt:" in response:
        await respond_with_image(update, response)


async def respond_with_image(update, response):
    prompt = response.split("\[prompt:")[1].split("\]")[0]
    await update.message.reply_text(f"Generating image with prompt `{prompt.strip()}`",
                                    parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)
    await application.bot.send_chat_action(update.effective_chat.id, "typing")
    photo = await drawWithStability(prompt)
    await update.message.reply_photo(photo=photo, caption=f"chatGPT generated prompt: {prompt}",
                                     parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)


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
    # with a timeout of 45 seconds, created a while loop that checks if loading is done
    loading = PAGE.query_selector_all("button[class^='PromptTextarea__PositionSubmit']>.text-2xl")
    #keep checking len(loading) until it's empty or 45 seconds have passed
    await application.bot.send_chat_action(update.effective_chat.id, "typing")
    start_time = time.time()
    while len(loading) > 0:
        if time.time() - start_time > 45:
            break
        time.sleep(0.5)
        loading = PAGE.query_selector_all("button[class^='PromptTextarea__PositionSubmit']>.text-2xl")
        await application.bot.send_chat_action(update.effective_chat.id, "typing")


def start_browser():
    PAGE.goto("https://chat.openai.com/")
    if not is_logged_in():
        print("Please log in to OpenAI Chat")
        print("Press enter when you're done")
        input()
    else:

        # on different commands - answer in Telegram
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("reload", reload))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("draw", draw))

        # on non command i.e message - echo the message on Telegram
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

        # Run the bot until the user presses Ctrl-C
        application.run_polling()

if __name__ == "__main__":
    start_browser()
