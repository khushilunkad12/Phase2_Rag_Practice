from google import genai
import os
from dotenv import load_dotenv

from retriever import retrieve_chunks

# ==========================================
# 1. Load Environment Variables
# ==========================================

def get_gemini_client():
    """
    Loads the Gemini client when needed.
    """

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found. Please add it to the .env file."
        )

    return genai.Client(api_key=api_key)
# ==========================================
# 3. Generate RAG Answer
# ==========================================

def generate_answer(query):
    """
    Retrieves relevant chunks and generates
    an answer using Gemini.

    Returns:
        answer
        metadatas
        documents
    """

    ids, documents, metadatas, distances = retrieve_chunks(query)

    # print("\nRetrieved Chunks:\n")

    # for i in range(len(documents)):
    #     print("=" * 60)
    #     print(f"Rank : {i + 1}")
    #     print(f"Distance : {distances[i]:.4f}")
    #     print(f"Source : {metadatas[i]['source']}")
    #     print(f"Chunk : {metadatas[i]['chunk_index']}")
    #     print()
    #     print(documents[i])
    #     print("=" * 60)

    # ==========================================
    # Build Context
    # ==========================================

    context = "\n\n".join(documents)

    # ==========================================
    # Prompt
    # ==========================================

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the information provided in the context below.

If the answer cannot be found in the context, reply exactly:

Not enough information in the uploaded documents.

Context:
{context}

Question:
{query}
"""

    # ==========================================
    # Gemini
    # ==========================================
    
    gemini_client = get_gemini_client()

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return (
    response.text,
    metadatas,
    documents,
    distances
)


# ==========================================
# 4. Main Function
# ==========================================

def main():

    query = input("Enter your question: ")

    if not query.strip():
        print("Question cannot be empty.")
        return

    answer, metadatas, _, _ = generate_answer(query)

    print("\n")
    print("=" * 70)
    print("FINAL ANSWER")
    print("=" * 70)
    print(answer)

    print("\n")
    print("=" * 70)
    print("SOURCES")
    print("=" * 70)

    for index, metadata in enumerate(metadatas, start=1):

        print(
            f"{index}. {metadata['source']} "
            f"(Chunk {metadata['chunk_index']})"
        )

    print("=" * 70)


# ==========================================
# 5. Entry Point
# ==========================================

if __name__ == "__main__":
    main()