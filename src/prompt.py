
from langchain_core.prompts import ChatPromptTemplate


rag_prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful AI assistant.

    Answer the question using only the provided context.

    If the answer cannot be found in the context,
    say "I don't know based on the provided documents."

    Do not make up information.

    Context:
    {context}

    Question:
    {question}

    Answer: 
    """
    )