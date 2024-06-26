from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_agent = update.message.from_user
    if not user_agent:
        await update.message.reply_text("Foydalanuvchi agenti aniqlanmadi!")
        return

    device_info = str(user_agent)  # user_agent-ni stringga aylantiramiz

    if 'Mobile' in device_info or 'Android' in device_info or 'iPhone' in device_info:
        message = """
        Hello! Welcome to Torcoin, the newest airdrop that allows users to earn cryptocurrency by simply clicking buttons. The bot is intuitive and convenient, which makes the process of receiving cryptocurrency as simple and accessible as possible.
        """
        keyboard = [
            [InlineKeyboardButton("Play Torcoin", web_app=WebAppInfo(url='https://tillo09.github.io/torcoin/'))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(message, reply_markup=reply_markup)
    else:
        await update.message.reply_text("Uzr, bu bot faqat mobil qurilmalar uchun mo'ljallangan.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
    Available commands:
    /start - Welcome message
    /help - List of commands
    """
    await update.message.reply_text(help_text)

if __name__ == '__main__':
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()
