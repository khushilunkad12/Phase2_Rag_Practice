import streamlit as st
import os
from main import process_documents
from embed_store import store_embeddings
from rag_answer import generate_answer
st.set_page_config(
    page_title="RAG Document QA",
    page_icon="📄",
    layout="wide"
)

st.title("📄 RAG Document Question Answering")

st.write(
    "Upload a document, process it, and ask questions using Retrieval-Augmented Generation (RAG)."
)

st.divider()

# ==========================================
# Upload Document
# ==========================================

uploaded_file = st.file_uploader(
    "Choose a document",
    type=["txt", "pdf"]
)

if uploaded_file is not None:

    # Create documents folder if it doesn't exist
    os.makedirs("documents", exist_ok=True)

    # Save uploaded file
    file_path = os.path.join(
        "documents",
        uploaded_file.name
    )

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.success(
        f"{uploaded_file.name} uploaded successfully!"
    )
    st.divider()

# ==========================================
# Process Document
# ==========================================

if uploaded_file is not None:

    if st.button("⚙️ Process Document"):

        with st.spinner("Processing document..."):

            process_documents()

            store_embeddings()

        st.success("Document processed successfully!")

st.divider()

# ==========================================
# Ask Question
# ==========================================

st.divider()

question = st.text_input(
    "Ask a question about your documents"
)

if st.button("🔍 Ask Question"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating answer..."):

            answer, sources, chunks, distances = generate_answer(
                question
            )

        st.success("Answer generated!")

        # ==========================================
        # Display Answer
        # ==========================================

        st.subheader("🤖 Answer")
        st.write(answer)

        # ==========================================
        # Display Sources
        # ==========================================

        st.subheader("📚 Sources")

        for index, source in enumerate(sources, start=1):

            st.write(
                f"{index}. {source['source']} "
                f"(Chunk {source['chunk_index']})"
            )

        # ==========================================
        # Display Retrieved Chunks
        # ==========================================

        st.subheader("📄 Retrieved Chunks")

        for i in range(len(chunks)):

            with st.expander(
                f"Chunk {i + 1} "
                f"(Distance: {distances[i]:.4f})"
            ):

                st.write(
                    f"**Source:** {sources[i]['source']}"
                )

                st.write(
                    f"**Chunk Index:** {sources[i]['chunk_index']}"
                )

                st.write(chunks[i])