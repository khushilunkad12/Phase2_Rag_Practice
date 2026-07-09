from document_loader import load_documents
from chunker import chunk_text

print("Running tests...\n")

# ==========================================
# Test 1 - Load Documents
# ==========================================

documents = load_documents("documents")

assert len(documents) > 0, "No documents were loaded."

print("✓ Documents loaded successfully.")

# ==========================================
# Test 2 - Chunk Documents
# ==========================================

all_chunks = []

for document in documents:

    chunks = chunk_text(
        document["text"],
        document["filename"]
    )

    all_chunks.extend(chunks)

assert len(all_chunks) > 0, "No chunks were created."

print("✓ Chunks created successfully.")

# ==========================================
# Test 3 - Validate Chunk Structure
# ==========================================

for chunk in all_chunks:

    assert "chunk_id" in chunk, "Chunk ID missing."

    assert "text" in chunk, "Chunk text missing."

    assert "metadata" in chunk, "Metadata missing."

print("✓ Chunk structure is valid.")

# ==========================================
# Test 4 - Validate Metadata
# ==========================================

for chunk in all_chunks:

    metadata = chunk["metadata"]

    assert "source" in metadata, "Source missing."

    assert "chunk_index" in metadata, "Chunk index missing."

    assert "chunk_size" in metadata, "Chunk size missing."

    assert "overlap" in metadata, "Overlap missing."

print("✓ Metadata validated.")

# ==========================================
# Test 5 - Validate Chunk Content
# ==========================================

for chunk in all_chunks:

    assert chunk["text"].strip() != "", "Empty chunk found."

print("✓ Chunk text validated.")

print("\n===================================")
print("All tests passed successfully!")
print("===================================")