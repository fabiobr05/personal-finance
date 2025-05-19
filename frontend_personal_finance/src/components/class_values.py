from ..data.init import init_db
import pandas as pd
import altair as alt
import streamlit as st

class ClassValue:
    def __init__(self):
        self.data = self._load_and_process_data()
        self.group_data = self._group_data()

    def _load_and_process_data(self):
        # Carregar os dados do banco de dados
        data = init_db()

        if data.empty:
            data = pd.DataFrame({
                'valor_total': pd.Series(dtype='float'),
                'classe_produto': pd.Series(dtype='str'),
            })

        # Garantir que o valor total seja numérico
        data['valor_total'] = pd.to_numeric(data['valor_total'], errors='coerce')
        return data

    def _group_data(self):
        # Agrupando pelos produtos e somando os valores totais
        group_data_raw = self.data[['classe_produto', 'valor_total']]
        group_data = group_data_raw.groupby(by='classe_produto').sum()
        group_data = group_data.reset_index().sort_values(by='valor_total', ascending=False)

        return group_data

    def show(self):
        chart = alt.Chart(self.group_data).mark_bar(color='#ef6e3b').encode(
            x=alt.X('classe_produto:N', sort='-y', axis=alt.Axis(labelAngle=-0)),  # Eixo X com classe_produto
            y='valor_total:Q',  # Eixo Y com valor_total
            text='valor_total:Q'  # Exibe o valor total no topo de cada barra
        ).properties(
            width=800,
            height=400
        ).configure_text(
            fontSize=12,  # Tamanho da fonte para os valores
            fontWeight='bold',
            color='black',  # Cor do texto (para garantir boa visibilidade)
            align='center',  # Alinha o texto ao centro da barra
            baseline='bottom'  # Faz o texto aparecer no topo das barras
        )

        # Mostrar o gráfico com os valores no topo das barras
        return st.altair_chart(chart, use_container_width=True)
