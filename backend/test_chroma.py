from services.chroma_db import add_documents

chunks = [
    "Python is a programming language.",
    "Machine learning uses data.",
    "FastAPI builds APIs."
]

add_documents(chunks)

print("Documents stored successfully!")