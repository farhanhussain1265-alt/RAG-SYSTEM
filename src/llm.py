from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

from src.config import OPENAI_API_KEY, GROQ_API_KEY

openai_llm=ChatOpenAI(
    model="gpt-5.6",
    api_key=OPENAI_API_KEY,
    temperature=0.2,
    max_tokens=1024
)


groq_llm=ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0.2,
    max_tokens=1024 
)