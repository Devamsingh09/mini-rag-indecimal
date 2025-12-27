import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def chunk_text(text, chunk_size=900):
    chunks, current = [], ""
    for sentence in text.split(". "):
        if len(current) + len(sentence) < chunk_size:
            current += sentence + ". "
        else:
            chunks.append(current.strip())
            current = sentence + ". "
    if current:
        chunks.append(current.strip())
    return chunks

def save_index(index, chunks, metadata, path="vector_store"):
    os.makedirs(path, exist_ok=True)
    faiss.write_index(index, f"{path}/index.faiss")
    with open(f"{path}/chunks.pkl", "wb") as f:
        pickle.dump((chunks, metadata), f)

def load_index(path="vector_store"):
    index = faiss.read_index(f"{path}/index.faiss")
    with open(f"{path}/chunks.pkl", "rb") as f:
        chunks, metadata = pickle.load(f)
    return index, chunks, metadata

def build_vector_store(documents):
    chunks, metadata = [], []
    for doc in documents:
        for chunk in chunk_text(doc["text"]):
            chunks.append(chunk)
            metadata.append(doc["id"])

    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings).astype("float32"))
    return index, chunks, metadata
