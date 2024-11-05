import requests

def main():
    try:
        response = requests.get("http://server-flask:5000")
        print("Resposta do servidor:", response.text)
    except requests.ConnectionError:
        print("Não foi possível conectar ao servidor.")

if __name__ == "__main__":
    main()
