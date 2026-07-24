# Will be using chromadb for vector database
import chromadb
import uuid
from services.embeddings import create_embedding

# Create a persistent database
client = chromadb.PersistentClient(path="./chroma_db")

# Retrieve a collection 
collection = client.get_or_create_collection(name="documents")

def add_documents(chunks):
    ids = [] 
    embeddings = []

    for chunk in chunks:
        ids.append(str(uuid.uuid4()))
        embeddings.append(create_embedding(chunk))
    
    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

def search_documents(question_embedding, k=3):
    results = collection.query(query_embeddings=[question_embedding], n_results=k)
    return results