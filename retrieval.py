import json
import faiss
import os
import numpy as np
from sentence_transformers import SentenceTransformer

# Ensure required directories exist
os.makedirs("models", exist_ok=True)

# Load sentence embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load Wikipedia dataset
with open("data/wikipedia_sample.json", "r") as f:
    texts = json.load(f)

# Convert text to embeddings
embeddings = embedding_model.encode(texts, convert_to_numpy=True)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, "models/faiss_index.bin")

print("✅ FAISS index successfully saved in models/faiss_index.bin")

def retrieve_docs(query, top_k=3):
    """Retrieve top-k relevant documents for a given query."""
    query_embedding = embedding_model.encode([query], convert_to_numpy=True)
    _, indices = index.search(query_embedding, top_k)
    return [texts[i] for i in indices[0]]
