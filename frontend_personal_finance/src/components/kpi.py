from ..data.init import init_db
import pandas as pd
import streamlit as st

class KPI:
    def __init__(self):
        self.data = self._load_and_process_data()

    def _load_and_process_data(self):
        # Load data from database
        data = init_db()
        
        if data.empty:
            data = pd.DataFrame({
                'valor_total': pd.Series(dtype='float')
            })

        data['valor_total'] = pd.to_numeric(data['valor_total'], errors='coerce')
        
        return data

    def show(self):
        # Display the full dataset as a table
        return st.dataframe(self.data)
    
    def show_kpi(self):
        # Calculate total value and number of transactions
        total_value = self.data['valor_total'].sum()
        total_count = self.data.shape[0]
        max_value = self.data['valor_total'].max()

        # Display KPIs in columns
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Value", f"R$ {total_value:,.2f}")
        col2.metric("Total Transactions", f"{total_count}")
        col3.metric("Max Transaction", f"R$ {max_value:,.2f}")
