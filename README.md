# bing-wallpaper
send daily bing wallpaper to a telegram channel

created by https://peapix.com/api

associated telegram channel of mine: https://t.me/BingWalls

## how to use:
- clone this repo
- create a telegram bot with BotFather and assign its token to `BINGWALLS_BOT_API` in environment variables
- create a telegram channel and put its id in `BING_WALLPAPERS_CHANNEL_USERNAME` environment variable (for me it's `@BingWalls`)
- make the created bot admin of the channel
- set this crontab interval for script (path should be edited):
```
0 */6 * * * /usr/bin/python3 /path/to/your/bing.py
```
