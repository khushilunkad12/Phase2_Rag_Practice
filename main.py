import json

from document_loader import load_documents
from chunker import chunk_text


# ==========================================
# Process Documents
# ==========================================

def process_documents():
    """
    Loads all documents, creates chunks,
    and saves them to output_chunks.json.
    """

    # ==========================================
    # Load all documents
    # ==========================================

    try:
        documents = load_documents("documents")
    except Exception as e:
        print(e)
        return

    print(f"Loaded {len(documents)} documents.\n")

    all_chunks = []

    # ==========================================
    # Chunk every document
    # ==========================================

    for document in documents:

        print(f"Processing: {document['filename']}")

        chunks = chunk_text(
            document["text"],
            document["filename"]
        )

        all_chunks.extend(chunks)

    # ==========================================
    # Save chunks
    # ==========================================

    with open(
        "output_chunks.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            all_chunks,
            file,
            indent=4
        )

    print("\nChunks saved to output_chunks.json")

    print(f"\nTotal Documents : {len(documents)}")
    print(f"Total Chunks    : {len(all_chunks)}\n")

    # ==========================================
    # Display chunks
    # ==========================================

    for chunk in all_chunks:

        print("=" * 60)
        print(f"Chunk ID    : {chunk['chunk_id']}")
        print(f"Source      : {chunk['metadata']['source']}")
        print(f"Chunk Index : {chunk['metadata']['chunk_index']}")
        print(f"Chunk Size  : {chunk['metadata']['chunk_size']} characters")
        print(f"Overlap     : {chunk['metadata']['overlap']} characters")
        print("\nText:\n")
        print(chunk["text"])
        print("=" * 60)
        print()

    return all_chunks


# ==========================================
# Main Function
# ==========================================

def main():
    process_documents()


# ==========================================
# Entry Point
# ==========================================

if __name__ == "__main__":
    main()