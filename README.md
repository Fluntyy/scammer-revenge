
# Scammer Revenge

Tools that spam a scammer's Telegram bot to make it rate limited

## Installation

1. First of all, you need to [download and install Python](https://python.org/downloads).
2. 
![Screenshot of Python Downloads page.](https://github.com/Fluntyy/scammer-revenge/assets/106996695/2f118958-ba70-4198-8af8-acfcf4acba15)

3. Install the required dependency.
```console
~/Scammer-Revenge$ pip install requests
```

3. Download and extract the latest `scammer-revenge-v.X.X.zip` [here](https://github.com/Fluntyy/scammer-revenge/releases/latest).
4. 
![Screenshot of Scammer Revenge releases page.](https://github.com/Fluntyy/scammer-revenge/assets/106996695/10c37635-880d-466f-8941-e5f1c8aad273)

5. Run `main.py`.
```console
~/Scammer-Revenge$ python main.py
```

## Usage
When you're running this tool for the first time, it will ask you for a token and Chat ID.
```
Configuration file not found. Please provide the following:
Enter your Telegram bot token: 
```

Enter a message that you want to send to the scammer, then this tool will spam the scammer's Telegram bot.

## FAQ

* **Q:** What do you mean by 'scammer'?
**A:** There is a scammer that spreads an APK that will forward all SMS and notification to the scammer using Telegram bot. This tool will rate limit the Telegram bot, so the scammer can't receive victim SMS and notification.

* **Q:** How do I get the token?
**A:** You will need to reverse-engineer scammer's APK virus to obtain the token.

## License

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)

