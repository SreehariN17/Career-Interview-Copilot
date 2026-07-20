from services.retrieval import retrieve
from services.llm import generate_response

# Retrieve the best chunk, build a prompt, 
# Send the prompt to gemini, return the answer
def answer_question(question, vector_store):
    chunk, score = retrieve(question, vector_store)
    prompt = f"""
    You are an interview assistant.
    Answer the interview question ONLY using the resume information below.
    If the answer is not contained in the resume, say that the information is not available. 

    Resume Information:
    {chunk}

    Interview Question:
    {question}
    """

    answer = generate_response(prompt)
    return answer