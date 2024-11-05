# 🎙️ Text-to-Speech Telegram Bot 🎙️

**⚠️ DISCLAIMER**: This script is intended for educational and personal use only. It provides text-to-speech conversion through Telegram to demonstrate bot capabilities with external APIs. **Unauthorized use that violates Telegram's Terms of Service or local regulations is strictly prohibited.**

## 📜 Overview
This bot allows users to convert text into speech! Just send a text message, and the bot will return an audio file of the spoken text. Built with Telegram’s Bot API, this bot integrates an external API to generate high-quality audio. 

## 🌟 Features
- 🎧 **Instant Text-to-Speech Conversion**: Send any text and get an audio response back in seconds.
- 🔊 **Realistic Voice Output**: Clear and natural-sounding audio.
- 💬 **Simple Usage**: Just send a message—no commands required!

## ⚙️ Setup and Installation

### Prerequisites
- **Python 3.7+** 🐍
- **Telegram Bot Token** from [BotFather](https://t.me/BotFather) 🔑

### Steps
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/yourusername/text-to-speech-bot.git
   cd text-to-speech-bot
   ```

2. **Install Required Libraries**:  
   ```bash
   pip install python-telegram-bot
   ```

3. **Set Up Your Bot Token**:  
   Replace `'YOUR_BOT_TOKEN'` in the `text-to-speech.py` file with your bot token from BotFather.

4. **Run the Bot**:  
   ```bash
   python text-to-speech.py
   ```

## 🚀 Usage
1. **Start the Bot**: Send `/start` to receive a welcome message.
2. **Convert Text to Speech**: Send any text message, and the bot will reply with an audio file of your text spoken aloud.

## 📌 Important Notes
- **API Source**: This bot uses the [Manzoor76b TTS API](https://text-to-speech.manzoor76b.workers.dev/) for voice generation.
- **Logging**: The bot logs each session for troubleshooting purposes.

## 🤝 Contribution
Feel free to fork the repository and make improvements! Pull requests are welcome.

## 📜 License
This project is licensed under the MIT License.

## ❤️ Acknowledgements
- **Telegram API** for seamless bot functionality.
- **Manzoor76b TTS API** for high-quality text-to-speech output.

--- 
