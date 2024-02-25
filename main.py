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

def save_config(token, chat_id, threads):
    config = ConfigParser()
    config['Configuration'] = {'Token': token, 'ChatID': chat_id, 'Threads': threads}
    with open('config.ini', 'w') as f:
        config.write(f)

config = load_config()

if config:
    token = config.get('Configuration', 'Token')
    chat_id = config.get('Configuration', 'ChatID')
    threads = config.get('Configuration', 'Threads')
else:
    print("Configuration file not found. Please provide the following:")
    token = input("Enter your Telegram bot token: ")
    chat_id = input("Enter the chat ID of the scammer: ")
    threads = 10
    confirmation = input("Would you like to save the configuration? (y/n) ")
    if confirmation == "y":
        save_config(token, chat_id, threads)
    else:
        pass

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

for _ in range(int(threads)):
    threading.Thread(target=send_message).start()