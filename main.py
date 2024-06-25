from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = """
Привет! Добро пожаловать в TorCoin.
Отныне ты — директор криптобиржи.
Какой? Выбирай сам. Тапай по экрану, собирай монеты, качай пассивный доход, разрабатывай собственную стратегию дохода.
Мы в свою очередь оценим это во время листинга токена, даты которого ты узнаешь совсем скоро.
Про друзей не забывай — зови их в игру и получайте вместе ещё больше монет!
"""
    keyboard = [
        [InlineKeyboardButton("Играть в 1 клик 🐹", web_app=WebAppInfo(url='https://github.com/tillo09/torcoin.git'))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message, reply_markup=reply_markup)

# Function to handle the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
Available commands:
/start - Welcome message
/help - List of commands
/price - Get the current price of TorCoin
"""
    await update.message.reply_text(help_text)

# Function to handle the /price command
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Here you can fetch the real price of TorCoin if it exists
    # For demonstration, we'll use a fictional price
    torcoin_price = 123.45  # Replace this with a real API call if available
    await update.message.reply_text(f"The current price of TorCoin is ${torcoin_price}")

# Your existing hello function
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# Main function to set up the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token("7150776976:AAEWTttcrYHP5cni9r52dYBbx8RAmvzBsdM").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("hello", hello))

    app.run_polling()
