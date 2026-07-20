from services.pdf import extract_text
from services.chunking import chunk_text
from services.embeddings import create_embedding

text = extract_text("data/sample_resume.pdf")

chunks = chunk_text(text, chunk_size=300, overlap=50)

embedding = create_embedding(chunks[0]) # Create embedding for the first chunk

print(f"Embedding length: {len(embedding)}")
print()
print(embedding[:10]) # Print the first 10 values of the embedding