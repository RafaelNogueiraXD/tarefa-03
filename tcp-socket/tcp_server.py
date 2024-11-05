import socket

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor (localhost)
PORT = 65432        # Porta para escutar as conexões

# Cria o socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Vincula o socket ao IP e porta
    server_socket.listen()            # Habilita o servidor para escutar conexões
    print(f"Servidor TCP escutando em {HOST}:{PORT}")

    # Aguarda uma conexão
    conn, addr = server_socket.accept()  # Aceita a conexão do cliente
    with conn:
        print(f"Conectado por {addr}")
        conn.sendall(b"Bem-vindo ao servidor!")  # Envia uma mensagem de boas-vindas
        while True:
            data = conn.recv(1024)  # Recebe dados do cliente (até 1024 bytes)
            if not data:
                break
            print(f"Recebido do cliente: {data.decode()}")  # Imprime a mensagem recebida
            conn.sendall(data)  # Envia de volta os dados recebidos (echo)
