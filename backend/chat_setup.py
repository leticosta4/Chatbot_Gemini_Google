import textwrap 
from backend.model import model
from IPython.display import Markdown
import re

chat = model.start_chat(history=[])
perguntas = []
respostas_html = []

def text_formatting(text):
    text = re.sub(r'^\*\*(.*?)\*\*', r'<strong>\1</strong>', text, flags=re.MULTILINE)
    text = re.sub(r'^\* (.*)', r'<li>\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', text, flags=re.DOTALL)
    text = text.replace('*', '')
    paragraphs = text.split('\n\n')
    paragraphs = [f'<p>{p}</p>' for p in paragraphs if p.strip()]
    return '\n'.join(paragraphs)


def fala_com_bot(prompt_recebida):
  perguntas.append(prompt_recebida)

  response = chat.send_message(prompt_recebida)
  print("Resposta: ", response.text, "\n")
  formated_response = text_formatting(response.text)

  respostas_html.append(formated_response)

  return formated_response

def mostra_historico():
   return zip(perguntas, respostas_html)

# def mostra_historico():
#   respostas_chat = []
#   perguntas_user = []
#   for parte in chat.history:
#       papel = parte.role
#       texto = parte.parts

#       if papel == "user":
#         perguntas_user.append(texto)
#       elif papel == "model": 
#         respostas_chat.append(texto)

#   for q, a in zip(perguntas_user, respostas_chat):
#     print(f"pergunta: {q}")
#     print(f" {texto}\n")
