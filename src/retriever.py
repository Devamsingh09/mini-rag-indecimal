import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def retrieve(query, index, chunks, metadata, top_k=5):
    import faiss
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb).astype("float32"), top_k)
    results = [(chunks[i], metadata[i]) for i in I[0]]

    keywords = query.lower().split()
    ranked = []
    for chunk, doc in results:
        score = sum(1 for w in keywords if w in chunk.lower())
        ranked.append((score, chunk, doc))
    ranked.sort(reverse=True)
    return [(c, d) for score, c, d in ranked]
