import streamlit as st
import requests

class CSVUploaderAPI:
    def __init__(self, api_url="http://localhost:8000/upload_csv/"):
        self.api_url = api_url

    def show(self):
        st.subheader("📤 Upload de Nota Fiscal (via API)")
        uploaded_file = st.file_uploader("Escolha um arquivo CSV com suas notas fiscais", type="csv")

        if uploaded_file is not None:
            try:
                files = {'file': (uploaded_file.name, uploaded_file, 'text/csv')}
                response = requests.post(self.api_url, files=files)

                if response.status_code == 200:
                    st.success("Dados enviados e inseridos com sucesso via API.")
                else:
                    st.error(f"Erro: {response.json().get('detail')}")
            except Exception as e:
                st.error(f"Erro na requisição: {str(e)}")
