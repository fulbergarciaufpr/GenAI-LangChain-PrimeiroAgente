from langchain_groq import ChatGroq
from dotenv import load_dotenv
from os import getenv

load_dotenv()
API_KEY = getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key = API_KEY,
    model        = "qwen/qwen3.8-27b",
    temperature  = 0.7
)

prompt = ""
while (True):
  prompt = input("Usuário: ")
  prompt = prompt.lower()

  if (prompt == "sair" or prompt == "exit"):
    break

  llm_answer = llm.invoke(prompt)
  edit_content = llm_answer.content.replace("\n\n", "\n").replace("\n", "\n     ")
  edit_content = "\nLLM: " + edit_content + "\n"
  print(edit_content)
