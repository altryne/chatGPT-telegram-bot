# ChatGPT Telegram Bot

* It uses playwright and chromium to open browser and parse html
* It is an unoffical api for development purpose only.


# How to install

* Make sure that python and virual environment is installed.

* Create a conda environment with `conda env create -f environment.yml`

* If you are installing playwright for the first time, it will ask you to run this command for one time only to download all the chrome software
```
playwright install
```

* Now run the server

```
python server.py
```

* The server runs at port `5001`. If you want to change, you can change it in server.py


# Credit

* Got started with this using [Daniel Gross's whatsapp gpt](https://github.com/danielgross/whatsapp-gpt) package.
