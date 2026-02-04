# Portfolio RAG System

## Overview
This portfolio is powered by a Retrieval-Augmented Generation (RAG) system.
Instead of static content, recruiters can interact with an AI assistant that
answers questions about my background, skills, and projects.

## Motivation
I wanted my portfolio to demonstrate real AI engineering skills, not just list them.
The goal was to build a system that:
- Represents my experience accurately
- Grounds answers in real project data
- Feels like a production AI product

## Architecture
- Knowledge Base: Markdown documents describing my projects, skills, and experience
- Embeddings: HuggingFace sentence-transformer embeddings
- Vector Database: ChromaDB (persistent)
- Retrieval: Semantic similarity search over project documents
- Generation: LLM (Groq-hosted model) using retrieved context

## How It Works
1. A recruiter asks a question via the chat interface
2. The system retrieves relevant documents from the vector database
3. Retrieved context is injected into a structured prompt
4. The LLM generates a grounded, evidence-based answer

## Why This Matters
This project demonstrates:
- Practical use of RAG beyond demos
- Clean separation of data, retrieval, and generation
- Production-minded design (persistent vector DB, API-based backend)
- Ability to explain systems clearly to non-technical stakeholders

## Technologies
- Python
- FastAPI
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq LLM API
