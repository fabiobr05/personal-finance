import sqlite3

BANK_PATH = './src/database/nfce.db'

# Criação da tabela
def init_db():
    conn = sqlite3.connect(BANK_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS qrcode_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nfce_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_compra TEXT,
            produto TEXT,
            codigo TEXT,
            quantidade INTEGER,
            unidade TEXT,
            valor_unitario REAL,
            valor_total REAL,
            comercio TEXT,
            cnpj TEXT,
            endereco TEXT,
            chave_acesso TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()