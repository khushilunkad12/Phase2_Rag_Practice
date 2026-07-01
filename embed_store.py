import json
import chromadb
from sentence_transformers import SentenceTransformer

# Load chunks from JSON
with open("output_chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

print(f"Loaded {len(chunks)} chunks.")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Embedding model loaded.")

# Create ChromaDB client
client = chromadb.Client()

# Create or get collection
collection = client.get_or_create_collection(
    name="rag_documents"
)

# Process each chunk
for chunk in chunks:

    # Generate embedding
    embedding = model.encode(chunk["text"]).tolist()

    # Store in ChromaDB
    collection.add(
        ids=[chunk["chunk_id"]],
        documents=[chunk["text"]],
        embeddings=[embedding],
        metadatas=[chunk["metadata"]]
    )

print("Embeddings stored successfully in ChromaDB.")