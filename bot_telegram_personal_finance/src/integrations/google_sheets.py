import gspread
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv

load_dotenv()

SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
SPREAD_SHEET_ID = os.getenv("SPREAD_SHEET_ID")
WORKSHEET_NAME = os.getenv("WORKSHEET_NAME")

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Autenticação
credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)
client = gspread.authorize(credentials)

def append_row_to_sheet(row_data):
    sheet = client.open_by_key(SPREAD_SHEET_ID)
    worksheet = sheet.worksheet(WORKSHEET_NAME)
    worksheet.append_row(row_data)
