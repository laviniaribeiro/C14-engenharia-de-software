import requests

def obter():
    url = "https://api.chucknorris.io/jokes/random"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()['value'] 
    else:
        return "Erro ao buscar piada."
    
if __name__ == "__main__":
    piada = obter()
    print("Piada do Chuck Norris:")
    print(piada)