from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

def get_chat_id(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    print(f"Chat ID: {chat_id}")
    update.message.reply_text(f"Chat ID: {chat_id}")

# Set up the Updater
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add a handler to get messages
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_chat_id))

# Start the bot
updater.start_polling()

# Keep the program running
updater.idle()
