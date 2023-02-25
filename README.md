# bing-wallpaper
send daily bing wallpaper to a telegram channel

created by https://peapix.com/api

associated telegram channel: https://t.me/BingWalls

## how to use:
- clone this repo
- set `BINGWALLS_BOT_API` and `BING_WALLPAPERS_CHANNEL_USERNAME` as env.
- set this crontab interval for script (path should be edited):
```
0 */6 * * * /usr/bin/python3 /path/to/your/bing.py
```
