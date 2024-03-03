# 🔑 How to Obtain Scammer's Token

## 📝 Prerequisites
Before you begin, make sure you have the following:
- Scammer's APK file (Android application package)
- A decompiler

## 🪜 Steps

1. **Obtain the Scammer's APK File**
   - You'll need the scammer's APK file. This file contains the scammer's application.
   - APK stands for Android Package. It's the format used to distribute and install applications on Android devices.

2. **Change the Extension from APK to ZIP**
   - Rename the scammer's APK file by changing the extension from `.apk` to `.zip`.
   - This step allows you to treat the APK file as a regular ZIP archive.

3. **Extract the classes3.dex File**
   - Open the ZIP file using any ZIP extraction tool (e.g., WinRAR, 7-Zip).
   - Extract the `classes3.dex` file from the archive.
   - This file contains the compiled Java code of the scammer's app.

4. **Decompile the classes3.dex File**
   - Visit [decompiler.com](https://decompiler.com/) (or any other online decompiler).
   - Drag and drop the `classes3.dex` file onto the website.
   - The decompiler will analyze the file and provide a list of Java classes.

5. **Locate the Token**
   - Browse through the file until you find a URL like:
     ```
     https://api.telegram.org/bot6961009684:AAHfTYXH-4qXIFwNCJ8-O0rHcCI1AGHVC5A/sendMessage?markdownV2&chat_id=6325903877&text=blabla
     ```
     - The random string after "bot..." is the **token**, for example: `6961009684:AAHfTYXH-4qXIFwNCJ8-O0rHcCI1AGHVC5A`.
     - The random number after "markdownV2&chat_id=..." is the **chat ID**, for example: `6325903877`.
     - Copy the token and chat ID to Scammer Revenge, and you're all set!
