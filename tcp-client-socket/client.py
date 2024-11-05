import socket
import time

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta do servidor

# Número de mensagens a serem enviadas
NUM_MESSAGES = 10000
MESSAGE = "ola"
# Cria o socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))  # Conecta ao servidor

    # Marca o tempo de início
    start_time = time.time()

    # Envia mensagens para o servidor
    for _ in range(NUM_MESSAGES):
        try:
            # Envia uma mensagem para o servidor
            print(f"Enviando mensagem para {HOST}:{PORT}")
            client_socket.sendall(MESSAGE.encode())

            # Recebe a resposta do servidor
            data = client_socket.recv(1024)
            print("Resposta do servidor:", data.decode())
        except Exception as e:
            print(f"Erro: {e}")
    # Marca o tempo de fim
    end_time = time.time()

    # Calcula o tempo total e o tempo médio por requisição
    total_time = end_time - start_time
    average_time = total_time / NUM_MESSAGES

    # Exibe o resultado
    print(f"Tempo total para {NUM_MESSAGES} requisições: {total_time:.2f} segundos")
    print(f"Tempo médio por requisição: {average_time:.5f} segundos")
