import os

peapix_url = 'https://peapix.com/bing/feed?country=au'
bot_url = "https://api.telegram.org/bot" + os.environ['BINGWALLS_BOT_API'] + "/"
chat_id = os.environ['BING_WALLPAPERS_CHANNEL_USERNAME']
log_channel_id = os.environ['LOG_CHANNEL_ID']
