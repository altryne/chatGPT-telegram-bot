# ChatGPT Telegram Bot

* It uses playwright and chromium to open browser and parse html
* It is an unoffical api for development purpose only.

![CleanShot 2022-12-02 at 16 08 27](https://user-images.githubusercontent.com/463317/205404516-56ea908e-dd31-4c53-acb7-15f9f6ed379f.gif)



# How to install

* Make sure that python and virual environment is installed.

* Create a conda environment with `conda env create -f environment.yml`

* If you are installing playwright for the first time, it will ask you to run this command for one time only to download all the chrome software
```
playwright install
```

You need to setup your telegram bot token [how to](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) and [user id](https://bigone.zendesk.com/hc/en-us/articles/360008014894-How-to-get-the-Telegram-user-ID-) in `.env` file.
Edit the .env.example file and rename it to .env and place your values in there. 


* Now run the server

```
python server.py
```

Then find your bot in telegram (you should have already created it with @botfather) and start chatting. 

# Credit

* Got started with this using [Daniel Gross's whatsapp gpt](https://github.com/danielgross/whatsapp-gpt) package.
