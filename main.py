from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = """
Привет! Добро пожаловать в TorCoin.
Отныне ты — директор криптобиржи.
Какой? Выбирай сам. Тапай по экрану, собирай монеты, качай пассивный доход, разрабатывай собственную стратегию дохода.
Мы в свою очередь оценим это во время листинга токена, даты которого ты узнаешь совсем скоро.
Про друзей не забывай — зови их в игру и получайте вместе ещё больше монет!
"""
    keyboard = [
        [InlineKeyboardButton("Play Torcoin", web_app=WebAppInfo(url='https://tillo09.github.io/torcoin/'))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message, reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
Available commands:
/start - Welcome message
/help - List of commands
/price - Get the current price of TorCoin
"""
    await update.message.reply_text(help_text)

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    torcoin_price = 123.45 
    await update.message.reply_text(f"The current price of TorCoin is ${torcoin_price}")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

if __name__ == '__main__':
    app = ApplicationBuilder().token("7150776976:AAEWTttcrYHP5cni9r52dYBbx8RAmvzBsdM").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("hello", hello))

    app.run_polling()
