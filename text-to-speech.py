import logging
import urllib.parse
from telegram import Update, Audio
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
BOT_TOKEN = '8055309047:AAG5zroSWkUIz6nOl9KYIgKJXB595beJB00'

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! Send me any text, and I'll convert it to speech for you note i am made by @abirxdhackz!"
    )

# Text-to-Speech message handler
async def tts_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Send 'typing...' action while processing
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    # Extract and encode the user's message
    query = urllib.parse.quote(update.message.text)

    # Generate the TTS API URL
    tts_api_url = f"https://text-to-speech.manzoor76b.workers.dev/?text={query}"

    try:
        # Send the audio response
        await context.bot.send_audio(
            chat_id=update.effective_chat.id,
            audio=tts_api_url,
            title="BJ Tricks",
            performer="BJ Tricks",
            caption="🎧 Hᴇʀᴇ ɪs ʏᴏᴜʀ ᴀᴜᴅɪᴏ! Fᴀsᴛ, ʀᴇᴀʟ, ᴀɴᴅ ᴄʟᴇᴀʀ—ʏᴏᴜʀ ᴛᴇxᴛ, ᴏᴜʀ ᴠᴏɪᴄᴇ."
        )
    except Exception as e:
        # Send an error message if something goes wrong
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"❌ <b>Error:</b> <i>{str(e)}</i>",
            parse_mode="HTML"
        )

# Main function to run the bot
def main():
    # Create an application instance with the bot token
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, tts_handler))

    # Start the bot
    application.run_polling()

# Entry point for the script
if __name__ == '__main__':
    main()
