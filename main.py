import json

from document_loader import load_documents
from chunker import chunk_text


def process_documents():
    """
    Loads all documents, chunks them,
    saves output_chunks.json,
    and returns processing statistics.
    """

    try:
        documents = load_documents("documents")

    except Exception as e:
        print(e)
        return None

    print(f"Loaded {len(documents)} documents.\n")

    all_chunks = []

    total_pages = 0

    # ==========================================
    # Chunk every document
    # ==========================================

    for document in documents:

        print(f"Processing: {document['filename']}")

        total_pages += len(document["pages"])

        for page in document["pages"]:

            chunks = chunk_text(
                text=page["text"],
                filename=document["filename"],
                page_number=page["page"]
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
    print(f"Total Pages     : {total_pages}")
    print(f"Total Chunks    : {len(all_chunks)}\n")

    # ==========================================
    # Return statistics
    # ==========================================

    return {
        "documents": len(documents),
        "pages": total_pages,
        "chunks": len(all_chunks)
    }


# ==========================================
# Main Function
# ==========================================

def main():

    stats = process_documents()

    if stats is None:
        return

    print("=" * 60)
    print("PROCESSING SUMMARY")
    print("=" * 60)
    print(f"Documents : {stats['documents']}")
    print(f"Pages     : {stats['pages']}")
    print(f"Chunks    : {stats['chunks']}")
    print("=" * 60)


# ==========================================
# Entry Point
# ==========================================

if __name__ == "__main__":
    main()