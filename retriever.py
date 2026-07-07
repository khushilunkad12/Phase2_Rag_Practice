import chromadb
from sentence_transformers import SentenceTransformer

# ==========================================
# 1. Load Embedding Model
# ==========================================

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded.")

# ==========================================
# 2. Connect to ChromaDB
# ==========================================

client = chromadb.PersistentClient(path="chroma_db")

try:
    collection = client.get_collection(
        name="rag_documents"
    )

except Exception:
    print("Error: Chroma collection not found.")
    print()
    print("Run the following first:")
    print("python main.py")
    print("python embed_store.py")
    exit()

print("Connected to ChromaDB.")


# ==========================================
# 3. Retrieval Function
# ==========================================

def retrieve_chunks(query, top_k=3):
    """
    Retrieves the most relevant chunks
    for the given user query.

    Returns:
        ids
        documents
        metadatas
        distances
    """

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    ids = results["ids"][0]
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    return ids, documents, metadatas, distances


# ==========================================
# 4. Main Function
# ==========================================

def main():

    query = input("Enter your question: ")

    if not query.strip():
        print("Question cannot be empty.")
        return

    ids, documents, metadatas, distances = retrieve_chunks(query)

    for i in range(len(documents)):

        print("=" * 60)
        print(f"Rank #{i + 1}")
        print(f"Chunk ID     : {ids[i]}")
        print(f"Distance     : {distances[i]:.4f}")

        metadata = metadatas[i]

        print(f"Source       : {metadata['source']}")
        print(f"Chunk Index  : {metadata['chunk_index']}")
        print(f"Chunk Size   : {metadata['chunk_size']}")
        print(f"Overlap      : {metadata['overlap']}")

        print("\nRetrieved Text:\n")
        print(documents[i])

        print("=" * 60)
        print()


# ==========================================
# 5. Entry Point
# ==========================================

if __name__ == "__main__":
    main()