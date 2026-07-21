from fastapi import FastAPI, UploadFile, File
from typing import List

from services.llm import generate_response
from services.document_processor import process_documents

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.rag import answer_question

class ChatRequest(BaseModel):
    message: str

app = FastAPI()

vector_store = None

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

@app.post("/upload")
async def upload_documents(files: List[UploadFile] = File(...)):

    global vector_store

    vector_store = process_documents(files)

    return {
        "message": "Documents processed successfully",
        "documents_uploaded": len(files)
    }

@app.post("/chat")
def chat(request: ChatRequest):
    if vector_store is None: 
        return {
            "response": "Please upload documents first."
        }

    response = answer_question(request.message, vector_store)
    return {
        "response": response
    }