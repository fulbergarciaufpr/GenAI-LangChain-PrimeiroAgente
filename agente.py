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

prompt = "Olá! Como vai você?"
print("Usuário:" + prompt + "\n")
llm_answer = llm.invoke(prompt)

print("Classe de retorno:", type(llm_answer), "\n")
print("Mensagem de retorno:\n" + llm_answer.content)
