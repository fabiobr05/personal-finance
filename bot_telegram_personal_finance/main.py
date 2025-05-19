from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler
from src.tools.telegram_tools.commands_bot import start, handle_photo
from src.database.init import init_db
import os
import uvicorn
import threading
from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI
from src.database import api_routes
app_api = FastAPI()
app_api.include_router(api_routes.router)



def run_fastapi():
    uvicorn.run(app_api, host="0.0.0.0", port=8000)



# Inicializa o bot
def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("Você precisa definir a variável de ambiente BOT_TOKEN.")
    
    # Inicia a API em uma thread separada
    threading.Thread(target=run_fastapi, daemon=True).start()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))


    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    init_db()
    main()
