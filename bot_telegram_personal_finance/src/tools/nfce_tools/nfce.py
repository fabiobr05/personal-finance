import requests
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings("ignore", category=UserWarning, message=".*XMLParsedAsHTMLWarning.*")

def extract_data_nfce(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Erro ao acessar a página: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'lxml')

    table = soup.find('table', {'id': 'tabResult'})
    if not table:
        print("Tabela de itens não encontrada.")
        return []

    rows = table.find_all('tr')
    cnpj_endereco = soup.find_all('div', class_='text') if soup.find('div', class_='txtTopo') else []

    cnpj = cnpj_endereco[0].text.strip()[5:] if cnpj_endereco else ''
    cnpj_limpo = cnpj.strip()

    endereco = cnpj_endereco[1].text.strip() if len(cnpj_endereco) > 1 else ''
    endereco_limpo = ' '.join([part.strip() for part in endereco.split(',') if part.strip()])

    data_compra = soup.find('div', id='infos').find('li').text.split('Emissão:')[1].split('-')[0].strip()

    comercio = soup.find('div', class_='txtTopo').text.strip() if soup.find('div', class_='txtTopo') else ''
    chave_acesso = soup.find('span', class_='chave').text.strip() if soup.find('span', class_='chave') else ''

    items = []
    for row in rows:
        columns = row.find_all('td')
        if len(columns) > 0:
            item = {
                "data_compra": data_compra,
                "produto": columns[0].find('span', class_='txtTit').text.strip() if columns[0].find('span', class_='txtTit') else '',
                "codigo": columns[0].find('span', class_='RCod').text.strip().replace("Código:", "").strip()[1:-1] if columns[0].find('span', class_='RCod') else '',
                "quantidade": int(columns[0].find('span', class_='Rqtd').text.strip().replace("Qtde.:", "").strip()) if columns[0].find('span', class_='Rqtd') else 0,
                "unidade": columns[0].find('span', class_='RUN').text.strip().replace("UN:", "").strip() if columns[0].find('span', class_='RUN') else '',
                "valor_unitario": float(columns[0].find('span', class_='RvlUnit').text.strip().replace("Vl. Unit.:", "").replace(',', '.')) if columns[0].find('span', class_='RvlUnit') else 0.0,
                "valor_total": float(columns[1].find('span', class_='valor').text.strip().replace('.', '').replace(',', '.')) if columns[1].find('span', class_='valor') else 0.0,
                "comercio": comercio,
                "cnpj": cnpj_limpo,
                "endereco": endereco_limpo,
                "chave_acesso": chave_acesso
            }
            items.append(item)

    return items
