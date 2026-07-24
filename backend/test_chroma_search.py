from services.chroma_db import search_documents
from services.embeddings import create_embedding

question = "Tell me about machine learning."

embedding = create_embedding(question)

results = search_documents(embedding)

print(results)

documents = results["documents"][0]
distances = results["distances"][0]

for i in range(len(documents)):
    print(f'\n Result {i+1}')
    print('-----------------')
    print(f'Distance: {distances[i]}')
    print(documents[i])