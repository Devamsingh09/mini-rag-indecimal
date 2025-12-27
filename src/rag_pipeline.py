import os
from src.load_docs import load_documents
from src.embedder import build_vector_store, save_index, load_index
from src.retriever import retrieve
from src.generator import generate_answer

class MiniRAG:
    def __init__(self):
        if os.path.exists("vector_store/index.faiss"):
            print("🔹 Loading cached FAISS index...")
            self.index, self.chunks, self.metadata = load_index()
        else:
            print("⚙️ Building embeddings from PDFs in /data ...")
            docs = load_documents()
            self.index, self.chunks, self.metadata = build_vector_store(docs)
            save_index(self.index, self.chunks, self.metadata)
            print("💾 Index saved for future use!")

    def ask(self, query):
        retrieved = retrieve(query, self.index, self.chunks, self.metadata)
        answer = generate_answer(retrieved, query)
        return retrieved, answer
