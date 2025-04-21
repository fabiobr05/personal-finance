FROM python:3.11-slim

# Instala dependências do sistema (incluindo suporte ao SQLite)
RUN apt-get update && apt-get install -y \
    build-essential \
    libzbar0 \
    libsqlite3-dev \
    sqlite3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

# Instala pacotes Python
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
