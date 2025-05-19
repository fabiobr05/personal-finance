import streamlit as st
from src.components import ProductDonutChart
from src.components import BusinessValue
from src.components import TableValues
from src.components import KPI
from src.components import ClassValue
from src.components import CSVUploaderAPI

def init_page():

    st.set_page_config(layout="wide")  # 👈 MUITO importante para usar a tela inteira

    st.write("""
    # 📈 Report - Personal Finance
    """)

    uploader = CSVUploaderAPI()
    uploader.show()

    KPI().show_kpi()

    # Use columns para organizar o layout
    kpi_col, chart_col = st.columns(2)

    with kpi_col:
        ProductDonutChart().show()

    with chart_col:
        BusinessValue().show()

    ClassValue().show()

    # Depois a tabela em tela cheia
    st.divider()
    TableValues().show()
