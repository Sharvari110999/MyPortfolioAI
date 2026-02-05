from vectorstore import load_vectorstore

if __name__ == "__main__":
    load_vectorstore(rebuild=True)
    print("✅ Vector DB built successfully")
