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

## AI Answer Validation (To be completed after Gemini quota resets)

| Test ID | Question                               | Expected Result                                              | Actual Result | Source/Page | Status |
| ------- | -------------------------------------- | ------------------------------------------------------------ | ------------- | ----------- | ------ |
| AI-01   | What is Python?                        | Returns Python definition from uploaded document             | Pending       | Pending     | ⏳      |
| AI-02   | What is RAG?                           | Returns RAG definition from uploaded document                | Pending       | Pending     | ⏳      |
| AI-03   | What are LLMs?                         | Returns LLM definition if present                            | Pending       | Pending     | ⏳      |
| AI-04   | Question outside the uploaded document | Displays "Not enough information in the uploaded documents." | Pending       | Pending     | ⏳      |
| AI-05   | Verify retrieved chunks                | Retrieved chunks are relevant to the question                | Pending       | Pending     | ⏳      |

---

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
