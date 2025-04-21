from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler
from src.telegram_tools.commands_bot import start, handle_photo
from src.database.init import init_db
import os
from dotenv import load_dotenv
load_dotenv()



# Inicializa o bot
def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("Você precisa definir a variável de ambiente BOT_TOKEN.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))


    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    init_db()
    main()
