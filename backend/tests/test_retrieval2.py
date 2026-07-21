from services.pdf import extract_text
from services.chunking import chunk_text
from services.vector_store import build_vector_store
from services.retrieval import retrieve 

text = extract_text("data/sample_resume.pdf")

chunks = chunk_text(text)

vector_store = build_vector_store(chunks)

questions = [
    "Tell me about your machine learning experience.",
    "What programming languages do you know?",
    "Tell me about your internship."
]

for question in questions:
    print('=' * 60)
    print(question)

    results = retrieve(question, vector_store, k=3)

    for result in results:
        print()
        print(f"Score:{round(result['score'],4)}")
        print(result['chunk'][:200])