from ..data.init import init_db
import pandas as pd
import streamlit as st

class TableValues:
    def __init__(self):
        self.data = self._load_and_process_data()

    def _load_and_process_data(self):
        # Load data from database
        data = init_db()

        if data.empty:
            data = pd.DataFrame({
                'data_compra': pd.Series(dtype='datetime64[ns]'),
                'classe_produto': pd.Series(dtype='str'),
                'produto': pd.Series(dtype='str'),
                'valor_total': pd.Series(dtype='float')
            })

        data['valor_total'] = pd.to_numeric(data['valor_total'], errors='coerce')

        final_data = data[['data_compra', 'classe_produto', 'produto', 'valor_total']]
        
        return final_data

    def show(self):
        # Display the full dataset as a table
        return st.dataframe(self.data)
