import socket
import time
REQUESTS = 10000
# Configurações do cliente
UDP_IP = "udp-server"  # Nome do container do servidor UDP
UDP_PORT = 6000
MESSAGE = "Olá, servidor UDP!"
start_time = time.time()

# Cria o socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for _ in range(REQUESTS):
    try:
        # Envia uma mensagem para o servidor
        print(f"Enviando mensagem para {UDP_IP}:{UDP_PORT}")
        sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

        # Recebe a resposta do servidor
        data, server = sock.recvfrom(1024)
        print("Resposta do servidor:", data.decode())
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        sock.close()
end_time = time.time()
total_time = end_time - start_time
average_time = total_time / REQUESTS
print(f"Tempo total para {REQUESTS} requisições: {total_time:.2f} segundos")
print(f"Tempo médio por requisição: {average_time:.5f} segundos")