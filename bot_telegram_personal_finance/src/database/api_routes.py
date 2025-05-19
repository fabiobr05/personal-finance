from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel, field_validator
import sqlite3
from typing import List
from pathlib import Path
from .csv_service import CSVService
import pandas as pd

router = APIRouter()

# Caminho do banco de dados
BASE_DIR = Path(__file__).resolve().parent
path_db = BASE_DIR / 'nfce.db'

class NFCEData(BaseModel):
    id: int = None
    data_compra: str
    classe_produto: str
    produto: str
    codigo: str
    quantidade: float
    unidade: str
    valor_unitario: float
    valor_total: float
    comercio: str
    cnpj: str
    endereco: str
    chave_acesso: str

    @field_validator('valor_unitario', 'valor_total', 'quantidade', mode='before')
    def parse_float_str(cls, v):
        if isinstance(v, str):
            return float(v.replace(',', '.'))
        return v

def get_connection():
    return sqlite3.connect(path_db)

@router.get("/nfce", response_model=List[NFCEData])
def read_nfces():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nfce_data")
    rows = cursor.fetchall()
    conn.close()
    return [NFCEData(**dict(zip([column[0] for column in cursor.description], row))) for row in rows]

@router.post("/nfce", response_model=NFCEData)
def create_nfce(data: NFCEData):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO nfce_data (data_compra, classe_produto, produto, codigo, quantidade, unidade, valor_unitario, valor_total, comercio, cnpj, endereco, chave_acesso)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (data.data_compra,
         data.classe_produto,
         data.produto,
         data.codigo,
         data.quantidade,
         data.unidade,
         data.valor_unitario,
         data.valor_total,
         data.comercio,
         data.cnpj,
         data.endereco,
         data.chave_acesso))
    conn.commit()
    data.id = cursor.lastrowid
    conn.close()
    return data

@router.put("/nfce/{nfce_id}", response_model=NFCEData)
def update_nfce(nfce_id: int, data: NFCEData):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE nfce_data SET
        chave_acesso = ?, data_compra = ?, cnpj = ?
        WHERE id = ?""",
        (data.chave_acesso, data.data_compra, data.cnpj, nfce_id))
    conn.commit()
    conn.close()
    data.id = nfce_id
    return data

@router.delete("/nfce/{nfce_id}")
def delete_nfce(nfce_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM nfce_data WHERE id = ?", (nfce_id,))
    conn.commit()
    conn.close()
    return {"message": "Nota deletada com sucesso"}

@router.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Arquivo deve ser um CSV.")
    
    try:
        contents = await file.read()
        df = pd.read_csv(pd.io.common.BytesIO(contents))
        service = CSVService()
        service.insert_csv(df)
        return {"message": "Dados inseridos com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
