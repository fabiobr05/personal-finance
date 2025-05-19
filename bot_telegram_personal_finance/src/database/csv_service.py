import pandas as pd
import sqlite3
from pathlib import Path

class CSVService:
    def __init__(self):
        self.db_path = Path(__file__).resolve().parent / "nfce.db"
        self.table_name = "nfce_data"

    def validate_columns(self, df: pd.DataFrame):
        expected_columns = [
            "data_compra", "classe_produto", "produto", "codigo", "quantidade", "unidade", "valor_unitario", "valor_total", "comercio", "endereco", "chave_acesso"
        ]
        return all(col in df.columns for col in expected_columns)

    def insert_csv(self, df: pd.DataFrame):
        if not self.validate_columns(df):
            raise ValueError("CSV inválido. As colunas não estão corretas.")
        
        with sqlite3.connect(self.db_path) as conn:
            df.to_sql(self.table_name, conn, if_exists="append", index=False)
