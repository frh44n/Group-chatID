from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import logging
import os

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get('TELEGRAM_TOKEN')
URL = os.environ.get('URL')

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
app = Flask(__name__)

# Create a dispatcher
dispatcher = Dispatcher(bot, None, use_context=True)

# Define the start function
def start(update: Update, context):
    update.message.reply_text('Hello! I will notify the group when I become an admin.')

# Define the handler for new chat members
def new_chat_members(update: Update, context):
    for new_member in update.message.new_chat_members:
        if new_member.id == context.bot.id:
            group_id = update.message.chat.id
            context.bot.send_message(chat_id=group_id, text=f'Thank you for promoting me to admin! The group ID is {group_id}.')

# Add handlers to the dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_chat_members))

# Define the route for webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

# Set webhook
bot.set_webhook(f'{URL}/webhook')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
