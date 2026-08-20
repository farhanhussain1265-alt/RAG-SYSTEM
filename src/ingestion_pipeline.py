from document_loader import load_pdf
from text_splitter import split_documents
from embedding import create_embeddings
from vector_store import add_documents

documents=load_pdf()

chunks=split_documents(documents)
print(f"total chunks {len(chunks)}")
texts=[chunk.page_content for chunk in chunks]

embeddings=create_embeddings(texts)
print(f"embedding shape :{embeddings.shape}")
add_documents(chunks,embeddings)
