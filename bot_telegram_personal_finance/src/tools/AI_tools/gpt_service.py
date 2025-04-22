from openai import OpenAI
import os
from dotenv import load_dotenv

# Carrega sua chave da OpenAI do arquivo .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def generate_prompt(descricao):
    return f"""
        Você é um especialista em supermercados. Sua tarefa é classificar produtos com base em sua descrição. Abaixo estão alguns exemplos de categorias:

        - Laticínios: leite, queijo, iogurte, margarina, leite condensado, creme de leite
        - Hortifrúti: tomate, cebola, limão, alface, brócolis, maçã, batata
        - Carnes: carne bovina, frango, peixe, carne de porco
        - Frios: presunto, salsicha, calabresa
        - Refrigerante: coca-cola, guaraná, fanta, soda, pepsi e outros
        - Cerveja: cerveja pilsen, cerveja artesanal, skol, brahma, heineken e outras
        - Bebidas Energeticas: redbull, monster e similares
        - Outras Bebidas: suco, água, chá, energético
        - Padaria e Massas: pão, pizza, macarrão, lasanha, massa de pão, esfiha
        - Doces e Guloseimas: bala, chocolate, chiclete, pirulito, paçoca, bombom
        - Sobremesas: gelatina, doce de leite, brigadeiro, sorvete, pudim
        - Produtos de Limpeza/Higiene: sabonete, shampoo, desodorante, papel higiênico, absorvente
        - Grãos e Cereais: arroz, feijão, milho verde, aveia, farinha
        - Molhos e Condimentos: ketchup, maionese, molho de tomate, pimenta, champignon
        - Outros: materiais escolares, utensílios domésticos, sacolas plásticas, copos descartáveis

        Com base nessa lógica, responda somente com o nome da categoria correspondente à descrição fornecida. Se não tiver certeza, retorne "Outros".

        Produto: {descricao}
    """


def classify_product(descricao):
    prompt = generate_prompt(descricao)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            { "role": "system", "content": "Você é um classificador de produtos de supermercado." },
            { "role": "user", "content": prompt }
        ],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()
