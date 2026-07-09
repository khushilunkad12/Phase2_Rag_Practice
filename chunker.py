import os
def chunk_text(text, source, chunk_size=300, overlap=50):
    """
    Splits text into chunks without breaking words.
    Adds metadata to every chunk.
    """

    chunks = []
    start = 0
    chunk_id = 1

    # Extract filename without extension
    source_name = os.path.splitext(
    os.path.basename(source)
)[0]

    while start < len(text):

        # Tentative end position
        end = start + chunk_size

        # If this is the last chunk
        if end >= len(text):
            end = len(text)

        else:
            # Move backward until a space is found
            while end > start and text[end] != " ":
                end -= 1

            # If no space found, split at chunk_size
            if end == start:
                end = start + chunk_size

        # Extract chunk
        chunk = text[start:end].strip()

        # Create formatted chunk ID
        formatted_chunk_id = f"{source_name}_chunk_{chunk_id:03d}"

        # Store chunk with metadata
        chunks.append({
            "chunk_id": formatted_chunk_id,
            "text": chunk,
            "metadata": {
                "source": source,
                "chunk_index": chunk_id,
                "chunk_size": len(chunk),
                "overlap": overlap
            }
        })

        # If last chunk, stop
        if end == len(text):
            break

        # Move start backwards for overlap
        start = end - overlap

        # Prevent negative index
        if start < 0:
            start = 0

        # Move forward to next complete word
        while start < len(text) and start > 0 and text[start - 1] != " ":
            start += 1

        chunk_id += 1

    return chunks