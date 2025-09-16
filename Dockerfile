# Usa imagem Python slim
FROM python:3.11-slim

# Instala Chrome para rodar Selenium
RUN apt-get update && apt-get install -y wget gnupg unzip && \
    wget -qO- https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-linux-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copia o código
COPY src/ src/

# comando padrão
CMD ["python", "src/bot.py", "Immanuel Kant", "artigo_kant.txt"]
