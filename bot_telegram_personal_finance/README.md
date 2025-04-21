# 🤖 Bot Telegram com Docker

Este projeto é um bot do Telegram construído com Python e empacotado com Docker. Ele pode ser facilmente executado com Docker Compose, bastando fornecer uma chave de API do Telegram Bot.

---

## 🧭 Passo a passo para executar

### 1. 🚀 Crie seu bot no Telegram

1. No Telegram, procure pelo [**BotFather**](https://t.me/botfather).
2. Envie o comando: /newbot
3. Escolha um nome para o bot (exemplo: `Meu Bot`).
4. Escolha um nome de usuário que termine com `bot` (exemplo: `meu_bot123`).
5. O BotFather vai te retornar uma **chave de API (token)** parecida com:
123456789:ABCdefGHIjkLmnoPQRstuVWxyz


⚠️ **Guarde essa chave com segurança.**

---

### 2. 📁 Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```
### 3. ✏️ Configure o arquivo .env
#### 3.1. Copie o arquivo .env.example:
```bash
cp .env.example .env
```
#### 3.2 Abra o arquivo .env e cole sua chave API no lugar certo:
```bash
BOT_TOKEN=123456789:ABCdefGHIjkLmnoPQRstuVWxyz
```
### 4. 🐳 Suba o container com Docker
Certifique-se de que você tenha o Docker e Docker Compose instalados. Depois, execute:
```bash
docker compose up --build
```

# Seu bot já estará rodando! ✅

📂 Estrutura do Projeto
.
├── src/                    # Código-fonte do bot
├── requirements.txt        # Dependências do Python
├── Dockerfile              # Define como o container é construído
├── .dockerignore           # Define arquivos a serem ignorados pelo docker
├── docker-compose.yml      # Define como o container roda
├── .env.example            # Exemplo de configuração de ambiente
└── README.md
└── main.py



🧰 Tecnologias
- Python 🐍
- python-telegram-bot
- Docker 🐳
- Docker Compose
