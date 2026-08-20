import chromadb
import hashlib

client=chromadb.PersistentClient(path="chroma_db")
collection=client.get_or_create_collection(
    name="rag_pdf_documents",
    metadata={"description":"vector store collection for pdf embedding in rag"}
)

def add_documents(chunks,embeddings):
    ids=[]
    chunks_content=[]
    all_metadata=[]
    embedding_list=[]

    for i,(chunk,embedding) in enumerate(zip(chunks,embeddings)):
        
        doc_id = hashlib.md5(
            chunk.page_content.encode("utf-8")
        ).hexdigest()
        ids.append(doc_id)

        metadata=dict(chunk.metadata)
        metadata["doc_idx"]=i
        metadata["page_length"]=len(chunk.page_content)
        all_metadata.append(metadata)

        chunks_content.append(chunk.page_content)

        embedding_list.append(embedding.tolist())

    collection.upsert(
            ids=ids,
            metadatas=all_metadata,
            documents=chunks_content,
            embeddings=embedding_list
    )

    print(f"added {len(chunks)} chunks to chromadb")



