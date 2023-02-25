import os

peapix_url = 'https://peapix.com/bing/feed?country=us'
bot_url = "https://api.telegram.org/bot" + os.environ['BINGWALLS_BOT_API'] + "/"
chat_id = os.environ['BING_WALLPAPERS_CHANNEL_USERNAME']
