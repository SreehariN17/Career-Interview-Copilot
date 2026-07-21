
from services.embeddings import create_embedding
import numpy as np

def cosine_similarity(vector1, vector2):
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)

    similarity = np.dot(vector1, vector2) / (
        np.linalg.norm(vector1) * np.linalg.norm(vector2)
    )

    return similarity

def retrieve(question, vector_store, k=3):
    question_embedding = create_embedding(question)

    similarities = []

    for item in vector_store:
        similarity = cosine_similarity(question_embedding, item['embedding'])
        
        similarities.append(
            {
                'score': similarity, 
                'chunk': item['chunk']
            }
        )
    
    similarities.sort(key=lambda x: x['score'], reverse=True)
    
    return similarities[:k]