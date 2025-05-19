import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Welcome message with registration button
def start(update: Update, context: CallbackContext) -> None:
    welcome_text = """
    🎲 Welcome to Vino Bingo! 🎲
    
    A thrilling money game where you can win big!
    
    First, please register to play.
    """
    
    # Create a keyboard with Register button
    keyboard = [
        [KeyboardButton("/register")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Registration process
def register(update: Update, context: CallbackContext) -> None:
    # Ask for phone number with contact button
    keyboard = [
        [KeyboardButton("Share Contact 📱", request_contact=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    update.message.reply_text(
        "To register, please share your phone number:",
        reply_markup=reply_markup
    )

# Handle contact sharing
def contact_handler(update: Update, context: CallbackContext) -> None:
    contact = update.message.contact
    user_id = update.message.from_user.id
    
    # Here you would normally save the contact info to a database
    # For now we'll just print it
    print(f"New registration: User {user_id}, Phone: {contact.phone_number}")
    
    # Send the web app button after registration
    keyboard = [
        [KeyboardButton("Open Vino Bingo 🎰", web_app=WebAppInfo(url="https://your-webapp-url.com"))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    update.message.reply_text(
        "✅ Registration complete!\n\nClick below to open Vino Bingo:",
        reply_markup=reply_markup
    )

def main():
    token = os.getenv('8117787100:AAHP8uShPCYnwijakNXBqdAAVKHqfYL-zq8')
    if not token:
        print("Error: No token found. Please set TELEGRAM_TOKEN environment variable.")
        return

    updater = Updater(token)
    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("register", register))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
