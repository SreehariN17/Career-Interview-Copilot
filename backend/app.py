from fastapi import FastAPI
from services.llm import generate_response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.pdf import extract_text
from services.chunking import chunk_text
from services.vector_store import build_vector_store
from services.rag import answer_question

class ChatRequest(BaseModel):
    message: str

app = FastAPI()

text = extract_text("data/sample_resume.pdf")
chunks = chunk_text(text)
vector_store = build_vector_store(chunks)

# Enable CORS in FastAPI (allow requests coming from React App)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Career Interview Copilot Backend is Running!"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    response = answer_question(request.message, vector_store)
    return {
        "response": response
    }