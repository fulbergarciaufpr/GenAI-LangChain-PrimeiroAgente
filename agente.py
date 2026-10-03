from langchain_groq import ChatGroq
from dotenv import load_dotenv
from os import getenv
import csv

load_dotenv()
API_KEY = getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key = API_KEY,
    model        = "qwen/qwen3.8-27b",
    temperature  = 0.7
)

csv_file = open("history.csv")
csv_reader = csv.reader(csv_file)
history = [tuple(row) for row in csv_reader]
csv_file.close()

prompt = ""
while (True):
  prompt = input("Usuário: ")
  prompt = prompt.lower()

  if (prompt == "sair" or prompt == "exit"):
    break

  history.append(("human", prompt.strip("\n").replace(",","")))
  llm_answer = llm.invoke(history)
  edit_content = llm_answer.content.replace("\n\n", "\n").replace("\n", "\n     ")
  edit_content = "\nLLM: " + edit_content + "\n"
  print(edit_content)
  history.append(("assistant", edit_content.strip("\n").replace(",","")))
  history.pop(1)
  history.pop(1)

csv_file = open("history.csv", "w")
for element in history:
  csv_file.write(element[0] + "," + element[1] + "\n")
csv_file.close()
