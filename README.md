# Chatbot_Gemini_Google
Programa de Chatbot simples com uso da API do Google Gemini AI, usando o modelo '`gemini-1.0-pro`', que trabalha somente com entrada de texto e é a última versão estável publicada.

### Principais bibliotecas e módulos utilizados
- [google.generativeai](https://ai.google.dev/gemini-api/docs/get-started/python#setup)  para uso da API do Gemini
- [re](https://docs.python.org/3/library/re.html)


### Criação de um ambiente virtual
 - Dentro da pasta do projeto, rodar no terminal:
    - python3 -m venv "nome do ambiente virtual"

 - Para ativar o ambiente virtual:
   - Linux:      source "nome do ambiente virtual"/bin/activate
   - Windows:    "nome do ambiente virtual"\Scripts\activate.bat


### Instalando as bibliotecas
Dentro da pasta do projeto, rodar no terminal:
    - pip install -r requirements.txt


### ATENÇÃO - Google API Key
- Clique aqui para gerar a sua [API Key](https://ai.google.dev/gemini-api/docs/api-key) 
- Após criar um arquivo chamado '`config.py`', na pasta '`backend/`', atribua o valor da sua chave gerada a uma váriavel de nome '`GOOGLE_API_KEY`'
    - Essa váriavel será importada nos módulos de setup do modelo para uso da API DO Gemini

