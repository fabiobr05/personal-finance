import sqlite3
from time import sleep

BANK_PATH = './src/database/nfce.db'

def save_nfce(data, class_product):
    conn = sqlite3.connect(BANK_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO nfce_data (
            data_compra, classe_produto, produto, codigo, quantidade, unidade,
            valor_unitario, valor_total, comercio, cnpj, endereco, chave_acesso
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['data_compra'],
        class_product,
        data['produto'],
        data['codigo'],
        data['quantidade'],
        data['unidade'],
        data['valor_unitario'],
        data['valor_total'],
        data['comercio'],
        data['cnpj'],
        data['endereco'],
        data['chave_acesso']
    ))
    conn.commit()
    conn.close()
