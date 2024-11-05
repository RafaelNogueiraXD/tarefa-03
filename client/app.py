import requests
import time
REQUESTS = 10000
def main():
    start_time = time.time()
    for _ in range(REQUESTS):
        try:
            response = requests.get("http://server-flask:5000")
            # print("Resposta do servidor:", response.text)
        except requests.ConnectionError:
            print("Não foi possível conectar ao servidor.")
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / REQUESTS

    print(f"Tempo total para {REQUESTS} requisições: {total_time:.2f} segundos")
    print(f"Tempo médio por requisição: {average_time:.5f} segundos")
if __name__ == "__main__":
    main()
