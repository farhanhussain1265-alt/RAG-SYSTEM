import chromadb
from src.embedding import create_embeddings
from sklearn.metrics.pairwise import cosine_similarity

client=chromadb.PersistentClient(path="chroma_db")

collection=client.get_collection(
    name="rag_pdf_documents"
)

def retrieve(query,top_k=5,score_thresold=0.0):
    # query=>embedding
    query_embeddings=create_embeddings([query])[0]
    
    # semantic searching
    results=collection.query(
        query_embeddings=[query_embeddings.tolist()],
        n_results=top_k
    )

    # cosine similarity
    retrieved_documents=[]
    if results["documents"] and results["documents"][0]:
        ids=results["ids"][0]
        metadatas=results["metadatas"][0]
        documents=results["documents"][0]
        distances=results["distances"][0]
        for i,(doc_id, metadata, document, distance) in enumerate(zip(ids,metadatas,documents,distances)):
            similarity_score=1-distance

            if similarity_score>score_thresold:
                retrieved_documents.append({
                    "id":doc_id,
                    "rank":i+1,
                    "document":document,
                    "metadata":metadata,
                    "distance":distance,
                    "similarity_score":similarity_score
                })
        print(f"length of retrieved_documents :{len(retrieved_documents)}")


    else:
        print("No documents founds")
    return retrieved_documents
