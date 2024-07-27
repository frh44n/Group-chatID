from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with your bot's token
TOKEN = 'YOUR_BOT_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

def handle_chat_member_update(update: Update, context: CallbackContext) -> None:
    chat_member = update.chat_member
    if chat_member.new_chat_member.status == 'administrator' and chat_member.new_chat_member.user.id == context.bot.id:
        chat_id = update.effective_chat.id
        context.bot.send_message(chat_id=chat_id, text=f'Hello! I am now an admin. The chat ID is {chat_id}.')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, handle_chat_member_update))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
