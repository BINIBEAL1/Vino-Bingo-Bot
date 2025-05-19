from telegram.ext import Updater, CommandHandler
import os

def start(update, context):
    update.message.reply_text('Hello! I am your bot. 🚀')

TOKEN = os.environ["TELEGRAM_TOKEN"]
updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
