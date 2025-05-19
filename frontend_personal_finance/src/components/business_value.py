from ..data.init import init_db
import pandas as pd
import altair as alt
import streamlit as st

class BusinessValue:
    def __init__(self):
        self.data = self._load_and_process_data()
        self.group_data = self._group_data()

    def _load_and_process_data(self):
        data = init_db()

        if data.empty:
            data = pd.DataFrame({
                'valor_total': pd.Series(dtype='float'),
                'comercio': pd.Series(dtype='str'),
            })


        data['valor_total'] = pd.to_numeric(data['valor_total'], errors='coerce')
        return data

    def _group_data(self):
        group_data_raw = self.data[['comercio', 'valor_total']]
        group_data = group_data_raw.groupby(by='comercio').sum()
        group_data = group_data.reset_index().sort_values(by='valor_total', ascending=False)

        # Quebra de linha se necessário (opcional)
        group_data['comercio'] = group_data['comercio'].apply(
            lambda x: '\n'.join(x[i:i+12] for i in range(0, len(x), 12))
        )

        return group_data

    def show(self):
        chart = alt.Chart(self.group_data).mark_bar(color='#9fbead').encode(
            x=alt.X('comercio:N', sort=None, axis=alt.Axis(labelAngle=-0)),
            y='valor_total:Q'
        ).properties(
            width=800,
            height=400
        )
        return st.altair_chart(chart, use_container_width=True)
