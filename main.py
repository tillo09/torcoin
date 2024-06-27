# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     message = """
#     Hello! Welcome to Torcoin, the newest airdrop that allows users to earn cryptocurrency by simply clicking buttons. The bot is intuitive and convenient, which makes the process of receiving cryptocurrency as simple and accessible as possible.
#     """
#     keyboard = [
#         [InlineKeyboardButton("Play Torcoin", web_app=WebAppInfo(url='https://tillo09.github.io/torcoin/'))],
#         [InlineKeyboardButton("Join our Telegram Channel", url='https://t.me/torcoins_community')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text(message, reply_markup=reply_markup)

# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     help_text = """
# Available commands:
# /start - Welcome message
# /help - List of commands
# """
#     await update.message.reply_text(help_text)

# if __name__ == '__main__':
#     app = ApplicationBuilder().token("7150776976:AAEWTttcrYHP5cni9r52dYBbx8RAmvzBsdM").build()

#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("help", help_command))

#     app.run_polling()



from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# Bot tokeningizni bu yerga kiriting
TOKEN = "7150776976:AAEWTttcrYHP5cni9r52dYBbx8RAmvzBsdM"
# Bot havolasi
BOT_LINK = 'https://t.me/torcoins_bot'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = """
    Hello! Welcome to Torcoin, the newest airdrop that allows users to earn cryptocurrency by simply clicking buttons. The bot is intuitive and convenient, which makes the process of receiving cryptocurrency as simple and accessible as possible.
    """
    keyboard = [
        [InlineKeyboardButton("Play Torcoin", web_app=WebAppInfo(url='https://tillo09.github.io/torcoin/'))],
        [InlineKeyboardButton("Join our Telegram Channel", url='https://t.me/torcoins_community')],
        [InlineKeyboardButton("Invite", callback_data='invite')]
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

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == 'invite':
        forward_message = f"Check out this bot: {BOT_LINK}"
        await context.bot.send_message(chat_id=query.message.chat_id, text=forward_message)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()




