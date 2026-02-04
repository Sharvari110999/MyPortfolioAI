# from fastapi import FastAPI
# from pydantic import BaseModel
# from rag import answer_question

# app = FastAPI(title="Sharvari Portfolio AI")

# class ChatRequest(BaseModel):
#     query: str

# @app.post("/chat")
# def chat(req: ChatRequest):
#     answer = answer_question(req.query)
#     return {"answer": answer}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag import answer_question

app = FastAPI(title="Sharvari Portfolio AI")

# CRITICAL: Add CORS so frontend can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
   # query: str
    message: str   # Support both fields

@app.get("/")
def root():
    return {"status": "online", "app": "Sharvari Portfolio AI"}

@app.post("/chat")
def chat(req: ChatRequest):
    answer = answer_question(req.message)
    return {
        "answer": answer,
        "response": answer
    }

@app.get("/health")
def health():
    return {"status": "healthy"}