import sqlite3
from time import sleep

BANK_PATH = './src/database/nfce.db'

# Função para salvar os dados
def save_qr_data(qr_data):
    conn = sqlite3.connect(BANK_PATH)
    cursor = conn.cursor()
    sleep(2)
    cursor.execute('INSERT INTO qrcode_data (content) VALUES (?)', (qr_data,))
    conn.commit()
    conn.close()
