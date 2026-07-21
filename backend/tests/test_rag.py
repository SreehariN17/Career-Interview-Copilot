from services.pdf import extract_text
from services.chunking import chunk_text
from services.vector_store import build_vector_store
from services.rag import answer_question

text = extract_text("data/sample_resume.pdf")
chunks = chunk_text(text)
vector_store = build_vector_store(chunks)

questions = [
    "Tell me about your machine learning experience.",
    "Why are you qualified for a software engineering internship?",
    "What programming languages do you know?",
    "Tell me about your projects."
]

for question in questions: 
    print("="*60)
    print(f"Question: {question}")
    print() 

    response = answer_question(question, vector_store)

    print(f"Answer: {response}")
    print()