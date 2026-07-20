from services.pdf import extract_text
from services.chunking import chunk_text
from services.vector_store import build_vector_store

text = extract_text("../sample_resume.pdf")
chunks = chunk_text(text, chunk_size=300, overlap=50)
vector_store = build_vector_store(chunks) 

print(f"Stored {len(vector_store)} vectors.\n")

print(vector_store[0].keys())  # Print the first vector entry
print()
print(vector_store[0]["chunk"])  # Print the first chunk
print()
print(vector_store[0]["embedding"][:10])  # Print the first 10 values of the first embedding