FROM python:3.12.7

# Copia o código do servidor UDP
COPY tcp_server.py /app/tcp_server.py

# Define o diretório de trabalho
WORKDIR /app

# Executa o servidor UDP
CMD ["python", "tcp_server.py"]