import socket

# Configurações do servidor
UDP_IP = "0.0.0.0"  # Escuta em todas as interfaces
UDP_PORT = 6000

# Cria o socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Servidor UDP iniciado e escutando na porta {UDP_PORT}")

# Loop para receber dados
while True:
    data, addr = sock.recvfrom(1024)  # Recebe até 1024 bytes de dados
    print(f"Mensagem recebida de {addr}: {data.decode()}")
    # Envia uma resposta para o cliente
    response = "Mensagem recebida no servidor UDP"
    sock.sendto(response.encode(), addr)