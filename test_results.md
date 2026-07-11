# RAG Document QA – Test Results

## Test Environment

* **Application:** RAG Document Question Answering
* **Vector Database:** ChromaDB
* **Embedding Model:** all-MiniLM-L6-v2
* **LLM:** Gemini 2.5 Flash
* **Supported Documents:** PDF, TXT

---

## Functional Test Cases

| Test ID | Scenario                                     | Expected Result                                                          | Actual Result | Source/Page | Status |
| ------- | -------------------------------------------- | ------------------------------------------------------------------------ | ------------- | ----------- | ------ |
| TC-01   | Upload a PDF document                        | Document uploads successfully                                            | Pass          | N/A         | ✅      |
| TC-02   | Upload a TXT document                        | Document uploads successfully                                            | Pass          | N/A         | ✅      |
| TC-03   | Process uploaded document                    | Chunks and embeddings are generated successfully                         | Pass          | N/A         | ✅      |
| TC-04   | Display current active document              | Uploaded document name is displayed                                      | Pass          | N/A         | ✅      |
| TC-05   | Replace existing document with a new upload  | Previous document is removed and only the latest document remains active | Pass          | N/A         | ✅      |
| TC-06   | Reset Session                                | Documents, ChromaDB, output chunks, and session state are cleared        | Pass          | N/A         | ✅      |
| TC-07   | Ask a question before processing a document  | User is prompted to process a document first                             | Pass          | N/A         | ✅      |
| TC-08   | Retrieved chunks remain collapsed by default | Chunks are displayed inside expandable sections                          | Pass          | N/A         | ✅      |
| TC-09   | Source citations                             | Source file, page number, and chunk number are displayed                 | Pass          | N/A         | ✅      |
| TC-10   | Unsupported document                         | Unsupported file types are rejected                                      | Pass          | N/A         | ✅      |

---


## Retrieval & Answer Validation

| Test ID | Question                           | Retrieval Result                                                            | LLM Result                                                                               | Source/Page               | Status |
| ------- | ---------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------- | ------ |
| AI-01   | What is Python?                    | Relevant chunks retrieved successfully                                      | Correct answer generated before quota exhaustion                                         | python notes.pdf (Page 1) | ✅ Pass |
| AI-02   | What is RAG?                       | Relevant chunks retrieved successfully                                      | Correct answer generated before quota exhaustion                                         | sample.txt / rag.txt      | ✅ Pass |
| AI-03   | What are LLMs?                     | Relevant chunks retrieved successfully                                      | Correct answer generated before quota exhaustion                                         | sample.txt                | ✅ Pass |
| AI-04   | Which embedding model is used?     | Retrieval completed, but uploaded documents did not contain the information | Returned "Not enough information in the uploaded documents."                             | ai models.txt             | ✅ Pass |
| AI-05   | What is ChromaDB?                  | Retrieval completed, but uploaded documents did not contain the information | Returned "Not enough information in the uploaded documents."                             | AI-MODELS-TASK-1.pdf      | ✅ Pass |
| AI-06   | Question outside uploaded document | Retrieval completed successfully                                            | Correctly identified insufficient information                                            | N/A                       | ✅ Pass |
| AI-07   | Gemini API quota exhausted         | Retrieved chunks and sources displayed successfully                         | Answer generation unavailable due to API quota; application handled the error gracefully | N/A                       | ✅ Pass |

### Verification Summary

* Document upload verified
* Automatic document processing verified
* PDF and TXT document support verified
* Chunk generation verified
* ChromaDB embedding storage verified
* Semantic retrieval verified
* Source citation (file, page, chunk) verified
* Expandable retrieved chunks verified
* Single active document workflow verified
* Reset Session functionality verified
* "Not enough information" handling verified
* Gemini API quota handling verified (application continues to show retrieved context and sources)


## Features Verified

* Single active document workflow
* Automatic document processing after upload
* PDF and TXT document support
* Character-based chunking with overlap
* Embedding generation using Sentence Transformers
* ChromaDB vector storage
* Semantic similarity search
* Retrieval-Augmented Generation (RAG)
* Source citations
* Page number citations
* Expandable retrieved chunks
* Session reset functionality
* "Not enough information" response for unsupported queries

---

## Notes

The AI answer validation section will be completed after the Gemini API quota is available again. The current implementation has been verified for document upload, processing, indexing, retrieval workflow, UI behavior, and session management.
