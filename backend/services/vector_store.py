from services.embeddings import create_embedding

def build_vector_store(chunks):
    # Creating a vector database (vector store) from the chunks and their embeddings
    vector_store = [] 

    for chunk in chunks:
        embedding = create_embedding(chunk)
        vector_store.append({
            "chunk": chunk,
            "embedding": embedding
        })

    return vector_store