from pathlib import Path
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage, convert_to_messages
from langchain_core.documents import Document

from dotenv import load_dotenv
import os
import glob
import tiktoken
import numpy as np
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sklearn.manifold import TSNE
import plotly.graph_objects as go
from groq import Groq

load_dotenv(override=True)

MODEL = "llama-3.1-8b-instant"
DB_NAME = str(Path(__file__).parent.parent / "vector_db")

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
#embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
RETRIEVAL_K = 10

SYSTEM_PROMPT = """
You are a knowledgeable, friendly assistant representing Sharvari's Portfolio.
You are chatting with a founder or Hiring manager of some company and you will convince them why Sharvari is hirable.
If relevant, use the given context to answer any question.
If you don't know the answer, say so.
Context:
{context}
"""

vectorstore = Chroma(persist_directory=DB_NAME, embedding_function=embeddings)
#retriever = vectorstore.as_retriever()
retriever = vectorstore.as_retriever(
    search_kwargs={"k": RETRIEVAL_K}
)

llm = Groq(api_key=os.getenv("GROQ_API_KEY"))


# def fetch_context(question: str) -> list[Document]:
#     """
#     Retrieve relevant context documents for a question.
#     """
#     return retriever.invoke(question, k=RETRIEVAL_K)

def fetch_context(question: str) -> list[Document]:
    return retriever.invoke(question)



def combined_question(question: str, history: list[dict] = []) -> str:
    """
    Combine all the user's messages into a single string.
    """
    prior = "\n".join(m["content"] for m in history if m["role"] == "user")
    return prior + "\n" + question


def answer_question(question: str, history: list[dict] = []):
    combined = combined_question(question, history)

    docs = fetch_context(combined)
    context = "\n\n".join(doc.page_content for doc in docs)

    system_prompt = SYSTEM_PROMPT.format(context=context)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]

    response = llm.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.2
    )

    return response.choices[0].message.content, docs

