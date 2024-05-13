from flask import Flask, render_template, request
from backend.chat_setup import fala_com_bot


app = Flask(__name__)

@app.route("/index") 
@app.route("/") 
def index(): 
     return render_template('index.html', resposta="null") 

@app.route('/enviar-prompt', methods=['GET', 'POST'])
def enviar_pergunta():
    prompt = request.form['prompt']
    print("Pergunta recebida:", prompt)
    resposta_bot = fala_com_bot(prompt_recebida=prompt)

    return render_template('index.html', resposta=resposta_bot)

@app.route("/sobre")
def sobre():
     return render_template("sobre.html")