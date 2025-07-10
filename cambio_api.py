import requests

def converter(valor, de="BRL", para="USD"):
    url = f"https://api.frankfurter.app/latest?from={de}&to={para}"
    resposta = requests.get(url)
    dados = resposta.json()

    if 'rates' in dados and para in dados['rates']:
        taxa = dados['rates'][para]
        return valor * taxa
    else:
        print("Erro ao obter taxa de câmbio:", dados)
        return None
