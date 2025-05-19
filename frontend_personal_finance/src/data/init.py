import requests
import pandas as pd

def init_db():
    response = requests.get("http://localhost:8000/nfce")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    return pd.DataFrame()




# import sqlite3
# import pandas as pd
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent
# path_db = BASE_DIR / '../../../bot_telegram_personal_finance/src/database/nfce.db'
# path_db = path_db.resolve()

# def init_db():
#     connection = sqlite3.connect(path_db)
#     # Read data from a table into a DataFrame
#     query = "SELECT * FROM nfce_data"
#     df_db = pd.read_sql_query(query, connection)
#     # print(df_db)
#     return df_db

# # init_db()