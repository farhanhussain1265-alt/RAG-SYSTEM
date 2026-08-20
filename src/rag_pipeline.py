from src.retriever import retrieve
from src.prompt import rag_prompt
from src.llm import openai_llm, groq_llm

def pipeline(query):

    # retrive documents
    retrieved_documents=retrieve(query)

    # create context
    context="\n".join(retrieved_document["document"] for retrieved_document in retrieved_documents) if retrieved_documents else ""
    if not context:
        print(f"we found no context related to this query")
        return None
    
    #prompt
    prompt=rag_prompt.invoke({
        "context":context,
        "question":query
    })

    # response 
    # for ChatOpenAI
    response=openai_llm.invoke(prompt)

    # for ChatGroq
    #response=llm.invoke([prompt.format(context=context,query=query)]) # expecting a list as prompt

    return response.content
    
    