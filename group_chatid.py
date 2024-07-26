from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'
# Replace 'YOUR_SERVER_URL' with your actual server URL
WEBHOOK_URL = f"https://YOUR_SERVER_URL/{BOT_TOKEN}"

app = Flask(__name__)
bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

def get_chat_id(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    print(f"Chat ID: {chat_id}")
    update.message.reply_text(f"Chat ID: {chat_id}")

# Add a handler to get messages
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_chat_id))

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook_handler():
    update = Update.de_json(request.get_json(), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route('/set_webhook', methods=['GET'])
def set_webhook():
    bot.set_webhook(url=WEBHOOK_URL)
    return "Webhook set successfully"

if __name__ == "__main__":
    app.run(port=5000)
