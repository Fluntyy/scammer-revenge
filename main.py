import requests
import threading
import time
import os
from configparser import ConfigParser

def load_config():
    config = ConfigParser()
    if os.path.isfile("config.ini"):
        with open('config.ini', 'r') as f:
            config.read_file(f)
        return config
    else:
        return None

def save_config(token, chat_id):
    config = ConfigParser()
    config['Configuration'] = {'Token': token, 'ChatID': chat_id}
    with open('config.ini', 'w') as f:
        config.write(f)

config = load_config()

if config:
    token = config.get('Configuration', 'Token')
    chat_id = config.get('Configuration', 'ChatID')
else:
    print("Configuration file not found. Please provide the following:")
    token = input("Enter your Telegram bot token: ")
    chat_id = input("Enter the chat ID of the scammer: ")
    save_config(token, chat_id)

message = input("Enter the message to send to the scammer: ")

url = f"https://api.telegram.org/bot{token}/sendMessage"
params = {
    "chat_id": chat_id,
    "text": message,
    "parse_mode": "markdown"
}

count = 0
error = False

def send_message():
    global count
    global error
    while True:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            count += 1
            print(f"\rSending messages... ({count})", end='', flush=True)
            error = False
        elif not error:
            print(f"\nError sending messages! {response.json().get('description')}")
            error = True
            if "Too Many Requests: retry after" in response.json().get('description'):
                time.sleep(int(''.join(filter(str.isdigit, response.json().get('description')))))
            else:
                os._exit(0)

threading.Thread(target=send_message).start()
threading.Thread(target=send_message).start()
threading.Thread(target=send_message).start()
threading.Thread(target=send_message).start()
threading.Thread(target=send_message).start()
threading.Thread(target=send_message).start()
threading.Thread(target=send_message).start()
threading.Thread(target=send_message).start()
threading.Thread(target=send_message).start()
threading.Thread(target=send_message).start()
