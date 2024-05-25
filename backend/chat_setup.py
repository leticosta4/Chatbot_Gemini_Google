from backend.model import model
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