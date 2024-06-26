

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# Global invite count
invites_count = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = """
    Hello! Welcome to Torcoin, the newest airdrop that allows users to earn cryptocurrency by simply clicking buttons. The bot is intuitive and convenient, which makes the process of receiving cryptocurrency as simple and accessible as possible.
    """
    keyboard = [
        [InlineKeyboardButton("Play Torcoin", web_app=WebAppInfo(url='https://tillo09.github.io/torcoin/'))]
        [InlineKeyboardButton("Join our Telegram Channel", url='https://t.me/torcoins_community')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message, reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
Available commands:
/start - Welcome message
/help - List of commands
/invite - Invite a friend to Torcoin
"""
    await update.message.reply_text(help_text)

async def invite_command(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in invites_count:
        invites_count[user_id] = 0

    invites_count[user_id] += 1
    await update.message.reply_text(f"Invitation sent! Your friend can join Torcoin using this link: https://tillo09.github.io/torcoin/")
    logging.info(f"User {user_id} invited a friend. Total invites: {invites_count[user_id]}")

if __name__ == '__main__':
    app = ApplicationBuilder().token("7150776976:AAEWTttcrYHP5cni9r52dYBbx8RAmvzBsdM").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("invite", invite_command))

    app.run_polling()
