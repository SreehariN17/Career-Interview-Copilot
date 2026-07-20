from services.pdf import extract_text
from services.chunking import chunk_text

text = extract_text("../sample_resume.pdf")

chunks = chunk_text(text, chunk_size=300, overlap=50)

print(f"Number of chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"----- Chunk {i + 1} -----")
    print(chunk)
    print()