
from services.embeddings import create_embedding
import numpy as np

def cosine_similarity(vector1, vector2):
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)

    similarity = np.dot(vector1, vector2) / (
        np.linalg.norm(vector1) * np.linalg.norm(vector2)
    )

    return similarity

def retrieve(question, vector_store):
    question_embedding = create_embedding(question)

    best_score = -1 
    best_chunk = None

    for item in vector_store:
        similarity = cosine_similarity(question_embedding, item["embedding"])
        
        if similarity > best_score: 
            best_score = similarity
            best_chunk = item["chunk"]
    
    return best_chunk, best_score
    