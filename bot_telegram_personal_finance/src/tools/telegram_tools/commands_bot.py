from telegram import Update
from telegram.ext import  ContextTypes
from pyzbar.pyzbar import decode
from PIL import Image
import tempfile
import os
import uuid

from ..database.qrcode_db import save_qr_data
from ..database.nfce_db import salvar_nfce
from ..nfce_tools.nfce import extract_data_nfce

# Função que será chamada com os dados do QR Code
def process_qr_data(qr_data: str):
    print("Conteúdo do QR Code:", qr_data)
    save_qr_data(qr_data)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name or "usuário"
    welcome_text = (
        f"Olá {user_first_name}, sou seu assistente de compras! 🛒\n\n"
        "Envie uma **nota fiscal com QR Code** da sua compra, e eu vou extrair os dados pra você."
    )
    await update.message.reply_text(welcome_text)


# Handler de mensagens com imagem
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()

    # Cria um nome de arquivo único
    temp_filename = f"temp_{uuid.uuid4().hex}.jpg"

    await file.download_to_drive(temp_filename)

    try:
        image = Image.open(temp_filename)
        decoded_objects = decode(image)

        if decoded_objects:
            for obj in decoded_objects:
                qr_data = obj.data.decode('utf-8')
                await update.message.reply_text(f'Dados do QR Code: {qr_data}')
                process_qr_data(qr_data)
                # Extrair dados da url
                nfce_data = extract_data_nfce(qr_data)

                for item in nfce_data:
                    salvar_nfce(item)

                resposta = f"Seus dados foram extraidos e armazenados com sucesso!!"
                await update.message.reply_text(resposta)

        else:
            await update.message.reply_text('Não encontrei nenhum QR Code na imagem.')
    finally:
        # Limpa o arquivo temporário
        if os.path.exists(temp_filename):
            os.remove(temp_filename)