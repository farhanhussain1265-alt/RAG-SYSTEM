# load pdf convert to documents
import os 
from langchain_community.document_loaders.pdf import PyMuPDFLoader


def load_pdf():
    folder_path="data/documents"
    num_doc=0
    all_documents=[]

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            pdf_path=os.path.join(folder_path,filename)

            try:
                loader=PyMuPDFLoader(pdf_path)
                documents=loader.load()
                all_documents.extend(documents)
                num_doc+=1
            except Exception as e:
                print(f"Error loading {pdf_path}: {e}")
    print("total document loaded:",num_doc)
    print("total pages loaded :",len(all_documents))
    return all_documents

documents=load_pdf()
print(type(documents))  
print("\nFirst page:")
print(documents[0].page_content[:500])