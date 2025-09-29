import requests

def testes():
    url_req = "https://api.chucknorris.io/jokes/random"
    resposta = requests.get(url_req, timeout=10)
    if resposta.status_code == 200:
        data = resposta.json()   
        return data['value']     
    else:
        return "Erro ao buscar piada."
    
if __name__ == "__main__":
    try:
        piada = testes()
    except Exception as e:
        print("Erro ao obter piada:", e)
    else:
        print("Piada do Chuck Norris:")
        print(piada)
