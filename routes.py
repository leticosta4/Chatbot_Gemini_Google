from flask import Flask, render_template, request
from backend.chat_setup import fala_com_bot, mostra_historico


app = Flask(__name__)

@app.route('/index') 
@app.route('/') 
def index(): 
     return render_template('index.html', resposta=None, pergunta=None) 

#ta dando problema aqui
@app.route('/historico', methods=['GET'])
def historico():
     historico = mostra_historico()
     return render_template("historico.html", history= historico)

@app.route('/enviar-prompt', methods=['POST'])
def enviar_pergunta():
    prompt = request.form['prompt']
    print("Pergunta recebida:", prompt)
    resposta_bot = fala_com_bot(prompt_recebida=prompt)

    return render_template('index.html', resposta=resposta_bot, pergunta=prompt)