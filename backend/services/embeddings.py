from services.llm import client

def create_embedding(text):
    response = client.models.embed_content(
        model = "gemini-embedding-001", 
        contents = text
    ) 

    return response.embeddings[0].values