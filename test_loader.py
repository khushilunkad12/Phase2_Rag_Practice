import os

from document_loader import load_documents
from chunker import chunk_text
from main import process_documents

print("Running tests...\n")

# ==========================================
# Test 1 - Load Multiple Documents
# ==========================================

documents = load_documents("documents")

assert len(documents) >= 2, "Expected at least 2 documents."

for document in documents:

    assert "filename" in document, "Filename missing."

    assert "pages" in document, "Pages missing."

print(f"✓ Loaded {len(documents)} documents successfully.")

# ==========================================
# Test 2 - Validate Pages Structure
# ==========================================

total_pages = 0

for document in documents:

    for page in document["pages"]:

        assert "page" in page, "Page number missing."

        assert "text" in page, "Page text missing."

        assert page["text"].strip() != "", "Empty page found."

        total_pages += 1

print(f"✓ Validated {total_pages} pages.")

# ==========================================
# Test 3 - Chunk All Documents
# ==========================================

all_chunks = []

for document in documents:

    for page in document["pages"]:

        chunks = chunk_text(
            text=page["text"],
            filename=document["filename"],
            page_number=page["page"]
        )

        all_chunks.extend(chunks)

assert len(all_chunks) > 0, "No chunks created."

print(f"✓ Created {len(all_chunks)} chunks.")

# ==========================================
# Test 4 - Validate Chunk Metadata
# ==========================================

for chunk in all_chunks:

    metadata = chunk["metadata"]

    assert "source" in metadata, "Source missing."

    assert "page" in metadata, "Page missing."

    assert "chunk_index" in metadata, "Chunk index missing."

    assert "chunk_size" in metadata, "Chunk size missing."

    assert "overlap" in metadata, "Overlap missing."

print("✓ Chunk metadata validated.")

# ==========================================
# Test 5 - Verify Multiple Sources
# ==========================================

sources = set(
    chunk["metadata"]["source"]
    for chunk in all_chunks
)

assert len(sources) >= 2, "Chunks should come from multiple documents."

print(f"✓ Chunks generated from {len(sources)} different documents.")

# ==========================================
# Test 6 - Run Full Processing Pipeline
# ==========================================

stats = process_documents()

assert stats is not None, "process_documents() returned None."

assert stats["documents"] >= 2, "Document count incorrect."

assert stats["pages"] > 0, "Page count should be greater than 0."

assert stats["chunks"] > 0, "Chunk count should be greater than 0."

assert os.path.exists(
    "output_chunks.json"
), "output_chunks.json was not created."

print("✓ Full processing pipeline validated.")

print("\n========================================")
print("All tests passed successfully!")
print("========================================")