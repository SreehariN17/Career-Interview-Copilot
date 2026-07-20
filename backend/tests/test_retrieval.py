from services.pdf import extract_text
from services.chunking import chunk_text
from services.vector_store import build_vector_store
from services.retrieval import retrieve

text = extract_text("../sample_resume.pdf")
chunks = chunk_text(text)
vector_store = build_vector_store(chunks)

question1 = "Tell me about your machine learning experience."
question2 = "What programming languages do you know?"
question3 = "Tell me about your internship."
question4 = "Where do you go to college?"

best_chunk, score = retrieve(question1, vector_store)
print(f"Question: {question1}")
print(f"Similarity Score: {score:.4f}\n")
print(f"Retrieved chunk: {best_chunk}")

best_chunk, score = retrieve(question2, vector_store)
print(f"Question: {question2}")
print(f"Similarity Score: {score:.4f}\n")
print(f"Retrieved chunk: {best_chunk}")

best_chunk, score = retrieve(question3, vector_store)
print(f"Question: {question3}")
print(f"Similarity Score: {score:.4f}\n")
print(f"Retrieved chunk: {best_chunk}")

best_chunk, score = retrieve(question4, vector_store)
print(f"Question: {question4}")
print(f"Similarity Score: {score:.4f}\n")
print(f"Retrieved chunk: {best_chunk}")