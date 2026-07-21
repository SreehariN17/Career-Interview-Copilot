from services.pdf import extract_text
from services.chunking import chunk_text
from services.vector_store import build_vector_store

def process_documents(files):
    all_chunks = []

    for file in files: 
        text = extract_text(file)
        chunks = chunk_text(text)
        all_chunks.extend(chunks)
    
    vector_store = build_vector_store(all_chunks)
    return vector_store