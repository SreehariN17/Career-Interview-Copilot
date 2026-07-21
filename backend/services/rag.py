from services.retrieval import retrieve
from services.llm import generate_response

# Retrieve the best chunk, build a prompt, 
# Send the prompt to gemini, return the answer
def answer_question(question, vector_store):
    retrieved_chunks = retrieve(question, vector_store, k=3)
    
    context = ""
    for item in retrieved_chunks:
        context += item['chunk'] + "\n\n"

    prompt = f"""
    You are an interview assistant.
    Answer ONLY using the provided context.
    If the answer cannot be found, say that the information is not available. 

    Resume Information:
    {context}

    Interview Question:
    {question}
    """

    answer = generate_response(prompt)
    return answer