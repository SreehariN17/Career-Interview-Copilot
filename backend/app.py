from fastapi import FastAPI
from services.llm import generate_response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str

app = FastAPI()

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
    response = generate_response(request.message)
    return {
        "response": response
    }