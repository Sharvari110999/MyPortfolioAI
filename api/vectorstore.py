import os
import glob
from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
KB_DIR = BASE_DIR / "knowledge-base"
DB_DIR = BASE_DIR / "vector_db"


# ----------------------------
# Vectorstore loader
# ----------------------------
def load_vectorstore(rebuild: bool = False):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # Reuse existing DB unless explicitly rebuilding
    if DB_DIR.exists() and not rebuild:
        return Chroma(
            persist_directory=str(DB_DIR),
            embedding_function=embeddings
        )

    # Optional clean rebuild (mirrors notebook delete_collection)
    if DB_DIR.exists() and rebuild:
        Chroma(
            persist_directory=str(DB_DIR),
            embedding_function=embeddings
        ).delete_collection()

    # ----------------------------
    # Load documents (EXACT notebook logic)
    # ----------------------------
    documents = []

    folders = glob.glob(str(KB_DIR / "*"))
    # print(f"Found {len(folders)} folders in knowledge base")

    for folder in folders:
        doc_type = os.path.basename(folder)

        loader = DirectoryLoader(
            folder,
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"}
        )

        folder_docs = loader.load()

        for doc in folder_docs:
            doc.metadata["doc_type"] = doc_type
            documents.append(doc)

    if not documents:
        raise RuntimeError("Knowledge base is empty — no documents loaded")

    # print(f"Loaded {len(documents)} documents")

    # ----------------------------
    # Chunking (same params as notebook)
    # ----------------------------
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)
    # print(f"Divided into {len(chunks)} chunks")

    # ----------------------------
    # Create vectorstore
    # ----------------------------
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(DB_DIR)
    )

    # ----------------------------
    # Optional inspection (like notebook)
    # ----------------------------
    collection = vectorstore._collection
    count = collection.count()

    sample_embedding = collection.get(
        limit=1,
        include=["embeddings"]
    )["embeddings"][0]

    dimensions = len(sample_embedding)

    # print(f"Vectorstore created with {count} vectors "f"({dimensions} dimensions)")

    return vectorstore
