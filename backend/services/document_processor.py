from services.pdf import extract_text
from services.chunking import chunk_text
from services.chroma_db import add_documents

def process_documents(files):
    all_chunks = []

    for file in files: 
        text = extract_text(file)
        chunks = chunk_text(text)
        all_chunks.extend(chunks)
    
    add_documents(all_chunks)
    return len(all_chunks)