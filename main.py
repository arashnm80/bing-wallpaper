import requests, json, os
from variables import peapix_url, bot_url, chat_id

def main():
    response = requests.get(peapix_url)
    if response.status_code == 200:
        # The request was successful
        data = response.json()  # Get the JSON data from the response
        date = data[0]["date"]
        imageUrl = data[0]["imageUrl"]
        print(date)
        print(imageUrl)
        if date_exists(date):
            print("This date already exists")
        else:
            with open("./dates/" + date, 'w') as file:
                file.write(imageUrl)
            send_to_channel(date)
    else:
        # The request failed
        print('Error:', response.status_code)

def date_exists(date):
    # Check if the file exists
    if os.path.isfile(date):
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
        'caption': "bing wallpaper of " + date
    })

    # Check if the message was sent successfully
    if response.status_code == 200:
        print('Image sent successfully!')
    else:
        print('Error sending image:', response.status_code)

    # send image as file:
    response = requests.post(bot_url + 'sendDocument', data={
        'chat_id': chat_id,
        'document': imageUrl,
        'caption': "high quality bing wallpaper of " + date
    })

    # Check if the message was sent successfully
    if response.status_code == 200:
        print('document sent successfully!')
    else:
        print('Error sending image:', response.status_code)

main()