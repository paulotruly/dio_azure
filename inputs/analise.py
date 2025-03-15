import requests

endpoint = ""
chave_api = ""

url = endpoint + "text/analytics/v3.0/sentiment"

texto = "Eu realmente adoro usar o Azure, é incrível!"

cabecalhos = {
    'Ocp-Apim-Subscription-Key': chave_api,
    'Content-Type': 'application/json'
}

corpo = {
    "documents": [
        {
            "id": "1",
            "language": "pt",
            "text": texto
        }
    ]
}

resposta = requests.post(url, headers=cabecalhos, json=corpo)
resultado = resposta.json()

print(resultado)
