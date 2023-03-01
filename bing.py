import requests, os
from variables import peapix_url, bot_url, chat_id, log_channel_id

def main():
    os.chdir(os.path.realpath(os.path.dirname(__file__))) # changes directory to path of bing.py so when I run script from another directory won't get error
    # these headers are used to make the request more natural like when it's from a user not a bot
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Referer': 'https://google.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    response = requests.get(peapix_url, headers=headers)
    if response.status_code == 200:
        # The request was successful
        data = response.json()  # Get the JSON data from the response
        date = data[0]["date"]
        imageUrl = data[0]["imageUrl"]
        print(date)
        print(imageUrl)
        if date_exists(date):
            print("date " + date + " already exists")
            log("date " + date + " already exists")
        else:
            with open("./dates/" + date, 'w') as file:
                file.write(imageUrl)
            send_to_channel(date)
    else:
        # The request failed
        print('Error: ' + response.status_code)
        log('Error: ' + response.status_code)

def date_exists(date):
    # Check if the file exists
    if os.path.isfile("./dates/" + date):
        return True
    else:
        return False

def send_to_channel(date):
    with open("./dates/" + date, 'r') as file:
        imageUrl = file.read()

    # send image
    response = requests.post(bot_url + 'sendPhoto', data={
        'chat_id': chat_id,
        'photo': imageUrl,
        'caption': "bing wallpaper of " + date + "\n\n" + chat_id
    })

    # Check if the message was sent successfully
    if response.status_code == 200:
        print('Image of ' + date + ' sent successfully!')
        log('Image of ' + date + ' sent successfully!')
    else:
        print('Error in sending image of ' + date + ' :' + response.status_code)
        log('Error in sending image of ' + date + ' :' + response.status_code)

    # send image as file:
    response = requests.post(bot_url + 'sendDocument', data={
        'chat_id': chat_id,
        'document': imageUrl,
        'caption': "high quality bing wallpaper of " + date + "\n\n" + chat_id
    })

    # Check if the message was sent successfully
    if response.status_code == 200:
        print('document of ' + date + ' sent successfully!')
        log('document of ' + date + ' sent successfully!')
    else:
        print('Error in sending document of ' + date + ' :' + response.status_code)
        log('Error in sending document of ' + date + ' :' + response.status_code)

def log(log_message):
    log = requests.post(bot_url + "sendMessage", data={
        "chat_id": log_channel_id,
        "text": log_message
    })

    # Check if the log was sent successfully
    if log.status_code == 200:
        print('log registered')
    else:
        print('Error in registering log:', log.status_code)

main()
