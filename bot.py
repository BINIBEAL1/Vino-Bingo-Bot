import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Your bot will respond to these commands
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot. How can I help?')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main():
    # Get the token from environment variables
    token = os.getenv('8117787100:AAHP8uShPCYnwijakNXBqdAAVKHqfYL-zq8')
    if not token:
        print("Error: No token found. Please set TELEGRAM_TOKEN environment variable.")
        return

    updater = Updater(token)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
