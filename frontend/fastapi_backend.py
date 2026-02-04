"""
FastAPI Backend for AI Portfolio
This file shows how to integrate your existing knowledge base with the portfolio frontend
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

# Initialize FastAPI app
app = FastAPI(title="AI Portfolio API", version="1.0.0")

# CRITICAL: Enable CORS so your frontend can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your Vercel domain: ["https://your-portfolio.vercel.app"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

# ============================================================================
# REPLACE THIS SECTION WITH YOUR ACTUAL KNOWLEDGE BASE LOGIC
# ============================================================================

def get_ai_response(user_message: str) -> str:
    """
    This is where you plug in your existing knowledge base!
    
    Replace this function with your actual implementation that:
    - Uses your vector database
    - Queries your LLM
    - Retrieves relevant information about you
    
    Example integration:
    
    from your_knowledge_base import query_knowledge_base
    
    def get_ai_response(user_message: str) -> str:
        # Your existing logic here
        context = retrieve_context_from_vectordb(user_message)
        response = query_llm_with_context(user_message, context)
        return response
    """
    
    # TEMPORARY MOCK RESPONSES - Replace with your actual knowledge base
    message_lower = user_message.lower()
    
    if "llm" in message_lower or "language model" in message_lower:
        return """I have strong experience with LLMs! I've developed 2 major projects using LLM APIs:

1. **LLM-Powered Chatbot** - Built using GPT-4 and LangChain with custom knowledge base integration, achieving 95% response accuracy
2. **AI Code Assistant** - Integrated Code Llama for intelligent code completion

I've also completed specialized courses in prompt engineering and fine-tuning. I'm confident in working with OpenAI, Anthropic, and open-source models."""
    
    elif "hackathon" in message_lower or "achievement" in message_lower or "prize" in message_lower:
        return """I've participated in multiple hackathons with great success:

🏆 **1st Place** - TechHack 2024 (LLM-Powered Chatbot)
🥈 **2nd Prize** - AI Innovation Summit (Document Intelligence System)
🏆 **Best AI Project** - HackFest 2024 (Real-time Sentiment Analyzer)
🎖️ **Finalist** - DevAI Hackathon (AI Code Assistant)

These experiences taught me rapid prototyping, team collaboration, and delivering production-ready AI solutions under pressure."""
    
    elif "skill" in message_lower or "tech" in message_lower:
        return """My technical skills span the full AI engineering stack:

**LLMs & APIs**: GPT-4, Claude, LangChain, OpenAI/Anthropic APIs
**ML/DL**: PyTorch, TensorFlow, Hugging Face, BERT, model fine-tuning
**Backend**: FastAPI, Python, REST APIs, WebSocket, Docker
**Vector DBs**: Pinecone, Chroma, PostgreSQL, Redis
**Frontend**: React, JavaScript, Gradio, Streamlit

I excel at building end-to-end AI applications from model training to deployment."""
    
    elif "project" in message_lower:
        return """I've built 4 major AI projects:

1. **LLM-Powered Chatbot** - RAG-based conversational AI with 95% accuracy
2. **Document Intelligence** - OCR + NLP for legal document analysis
3. **Sentiment Analyzer** - Real-time BERT-based analysis processing 10k+ messages/min
4. **AI Code Assistant** - IDE-integrated code completion and bug detection

Each project won recognition at hackathons and demonstrates production-grade AI engineering skills."""
    
    elif "experience" in message_lower or "work" in message_lower:
        return """I have 9 months of hands-on AI engineering experience, including:

- Building production LLM applications with custom knowledge bases
- Implementing RAG (Retrieval Augmented Generation) systems
- Fine-tuning transformer models for domain-specific tasks
- Deploying scalable AI APIs with FastAPI
- Winning multiple hackathon competitions

I'm proficient in the full AI development lifecycle from research to deployment."""
    
    elif "confident" in message_lower or "strong" in message_lower:
        return """Based on my track record:

✅ **LLMs**: Very confident - 2 production projects + specialized coursework
✅ **ML/DL**: Strong - Built custom models with 89-95% accuracy
✅ **Backend APIs**: Proficient - FastAPI, REST, WebSocket
✅ **Full-stack AI**: Capable - End-to-end project delivery
✅ **Hackathons**: Proven winner - Multiple 1st/2nd place finishes

My projects demonstrate both technical depth and ability to ship complete AI solutions."""
    
    else:
        return f"""I'm an AI Engineer with 9 months of experience building intelligent applications. I specialize in:

- Large Language Models (LLMs) and prompt engineering
- Machine Learning & Deep Learning with PyTorch/TensorFlow
- Building production AI APIs with FastAPI
- Vector databases and RAG systems

I've won prizes at multiple hackathons and built 4 major AI projects. Feel free to ask me about:
- My technical skills
- Project details
- Hackathon achievements
- LLM experience
- Specific technologies

What would you like to know?"""

# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "message": "AI Portfolio API is running",
        "version": "1.0.0"
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint that your frontend calls
    
    Receives a message and returns AI-generated response based on knowledge base
    """
    try:
        if not request.message or not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        # Get response from your knowledge base
        ai_response = get_ai_response(request.message)
        
        return ChatResponse(response=ai_response)
    
    except Exception as e:
        # Log the error (in production, use proper logging)
        print(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "endpoints": {
            "chat": "/chat",
            "health": "/health"
        }
    }

# ============================================================================
# EXAMPLE: How to integrate your existing Gradio knowledge base
# ============================================================================

"""
If you have a Gradio interface, you probably have something like:

def chat_function(message, history):
    # Your knowledge base logic
    response = query_vectordb_and_llm(message)
    return response

import gradio as gr
gr.ChatInterface(chat_function).launch()


To integrate with FastAPI:

1. Extract the core logic from chat_function
2. Put it in get_ai_response() above
3. Remove Gradio dependency for the API version

Example:

# your_knowledge_base.py
def query_knowledge_base(message: str) -> str:
    # Your vector DB retrieval
    context = vectordb.query(message)
    
    # Your LLM prompt
    prompt = f"Based on this context: {context}\n\nAnswer: {message}"
    
    # Your LLM call
    response = openai.ChatCompletion.create(...)
    
    return response

# Then in main.py:
from your_knowledge_base import query_knowledge_base

def get_ai_response(user_message: str) -> str:
    return query_knowledge_base(user_message)
"""

# ============================================================================
# RUN THE SERVER
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    # Development
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True  # Auto-reload on code changes
    )
    
    # Production: Use gunicorn or uvicorn without reload
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=4)
