## Problema de Acesso ao Language Studio:
Infelizmente, o **Azure Language Studio** só está disponível para **contas corporativas ou de estudante**. Eu encontrei esse problema ao tentar acessar a interface visual do Language Studio, e como eu não tenho uma conta corporativa ou de estudante, não consegui utilizá-lo diretamente.

No entanto, continuei utilizando o serviço de **Text Analytics API** do Azure através de **chamadas diretas à API** (como demonstrado neste projeto). Basta ter uma conta no **Azure**, criar o serviço **Text Analytics** e utilizar as **chaves da API**.

Se você já tem a chave e o endpoint, pode usar o código sem problemas, como mostrado acima.

# Análise de sentimentos com Azure Cognitive Services

Este projeto utiliza a API de **Análise de Sentimentos** do **Azure Cognitive Services** para determinar o sentimento de um texto fornecido. O Azure analisa o texto e fornece um score de confiança para sentimentos **positivos**, **neutros** e **negativos**.

## Tecnologias utilizadas:
- Python 3.x
- Azure Cognitive Services (Text Analytics API)
- Biblioteca `requests` para chamadas HTTP

## Como funciona:

O código realiza uma análise de sentimentos usando a API do Azure, que retorna uma resposta com a classificação do sentimento do texto (positivo, neutro ou negativo) e os scores de confiança.

### Explicação do Resultado:
- **`sentiment: 'positive'`**: O sentimento geral do texto foi classificado como **positivo**.
- **`confidenceScores`**: 
  - **`positive: 0.98`**: 98% de confiança de que o sentimento é positivo.
  - **`neutral: 0.02`**: 2% de chance de ser neutro.
  - **`negative: 0.0`**: Não há nenhum sentimento negativo no texto.
- **`sentences`**: A análise foi feita em cada frase individualmente. No caso, a frase "Eu realmente adoro usar o Azure, é incrível!" foi classificada como positiva.

### Conclusão:
Com este projeto, você consegue realizar **análise de sentimentos** em qualquer texto utilizando a **API do Azure**. Embora o **Language Studio** só esteja disponível para contas corporativas ou de estudante, ainda é possível utilizar a API diretamente com uma conta no **Azure**.

Se tiver alguma dúvida ou precisar de mais ajuda, sinta-se à vontade para entrar em contato!

### Exemplo de resultado:
```json
{
  "documents": [
    {
      "id": "1",
      "sentiment": "positive",
      "confidenceScores": {
        "positive": 0.98,
        "neutral": 0.02,
        "negative": 0.0
      },
      "sentences": [
        {
          "sentiment": "positive",
          "confidenceScores": {
            "positive": 0.98,
            "neutral": 0.02,
            "negative": 0.0
          },
          "offset": 0,
          "length": 44,
          "text": "Eu realmente adoro usar o Azure, é incrível!"
        }
      ],
      "warnings": []
    }
  ],
  "errors": [],
  "modelVersion": "2025-01-01"
}

