import textwrap 
from backend.model import model
from IPython.display import display
from IPython.display import Markdown

chat = model.start_chat(history=[])

def to_markdown(text):
  text = text.replace('•', ' **')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def fala_com_bot(prompt_recebida):
  response = chat.send_message(prompt_recebida)
  print("Resposta: ", response.text, "\n")
  md_response = to_markdown(response.text)
  return md_response.data
