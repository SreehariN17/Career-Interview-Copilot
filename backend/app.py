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
    chunks_added = process_documents(files)

    return {
        "message": "Documents processed successfully",
        "documents_uploaded": len(files),
        "chunks_added": chunks_added
    }

@app.post("/chat")
def chat(request: ChatRequest):
    response = answer_question(request.message)
    return {
        "response": response
    }