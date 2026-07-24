from services.retrieval import retrieve
from services.llm import generate_response
from services.embeddings import create_embedding
from services.chroma_db import search_documents

# Retrieve the best chunk, build a prompt, 
# Send the prompt to gemini, return the answer
def answer_question(question):
    # Create embedding for user's question
    question_embedding = create_embedding(question)

    # Search ChromaDB
    results = search_documents(question_embedding, k=3)

    # Extract retrieved documents
    documents = results["documents"][0]
    
    # Combine into one context string
    context = "\n\n".join(documents)

    prompt = f"""
    You are an interview assistant.
    Answer ONLY using the provided context.
    If the answer cannot be found in the provided context, say "The uploaded documents do not contain that information."
    
    Resume Information:
    {context}

    Interview Question:
    {question}
    """

    answer = generate_response(prompt)
    return answer