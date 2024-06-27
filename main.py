from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = """
    Hello! Welcome to Torcoin, the newest airdrop that allows users to earn cryptocurrency by simply clicking buttons. The bot is intuitive and convenient, which makes the process of receiving cryptocurrency as simple and accessible as possible.
    """
    keyboard = [
        [InlineKeyboardButton("Play Torcoin", web_app=WebAppInfo(url='https://tillo09.github.io/torcoin/'))],
        [InlineKeyboardButton("Join our Telegram Channel", url='https://t.me/torcoins_community')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message, reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
Available commands:
/start - Welcome message
/help - List of commands
"""
    await update.message.reply_text(help_text)

if __name__ == '__main__':
    app = ApplicationBuilder().token("7150776976:AAEWTttcrYHP5cni9r52dYBbx8RAmvzBsdM").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()





