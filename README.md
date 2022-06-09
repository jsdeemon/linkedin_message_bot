# Linkedin Bot (Python + Selenium)
## Automatically searches people and connects to them with message

### You can use any web browser. Example Download gecko driver for linux 
```bash
$ wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz
$ tar -xvzf geckodriver-v0.31.0-linux64.tar.gz
$ chmod +x geckodriver

$ export PATH=$PATH:/path-to-extracted-file/.
```
### Installing virtualenv and run the script
```bash 
$ virtualenv venv 
$ pip install selenium
$ source venv/bin/activate
```
### Run bot
```bash
$ python bot.py
```

