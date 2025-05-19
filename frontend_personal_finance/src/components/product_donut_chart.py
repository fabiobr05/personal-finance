from ..data.init import init_db
import pandas as pd
import altair as alt
import streamlit as st

class ProductDonutChart:
    def __init__(self):
        self.data = self._load_and_process_data()
        self.top_data = self._get_top_5_classes()

    def _load_and_process_data(self):
        data = init_db()

        if data.empty:
            data = pd.DataFrame({
                'valor_total': pd.Series(dtype='float'),
                'classe_produto': pd.Series(dtype='str'),
            })

        # Convert valor_total to numeric if needed
        data['valor_total'] = pd.to_numeric(data['valor_total'], errors='coerce')
        return data

    def _get_top_5_classes(self):
        group = self.data.groupby('classe_produto')['valor_total'].sum().reset_index()
        top5 = group.sort_values(by='valor_total', ascending=False).head(5)

        # Calculate percentage for labels
        total = top5['valor_total'].sum()
        top5['percentual'] = (top5['valor_total'] / total * 100).round(1)

        return top5

    def show(self):
        chart = alt.Chart(self.top_data).mark_arc(innerRadius=100).encode(
            theta=alt.Theta(field="valor_total", type="quantitative"),
            color=alt.Color(field="classe_produto", type="nominal", legend=alt.Legend(title="Classe Produto")),
            tooltip=[
                alt.Tooltip("classe_produto", title="Classe"),
                alt.Tooltip("valor_total", title="Valor Total", format=",.2f"),
                alt.Tooltip("percentual", title="%", format=".1f")
            ]
        ).properties(
            width=380,
            height=380,
            title="Top 5 Classes por Valor Total"
        )

        return st.altair_chart(chart, use_container_width=True)
