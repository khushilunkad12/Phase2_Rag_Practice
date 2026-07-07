import os
from pypdf import PdfReader


def read_txt(file_path):
    """
    Reads a text file and returns its contents.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def read_pdf(file_path):
    """
    Reads a PDF file and extracts text from every page.
    """

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def load_documents(folder_path):
    """
    Loads every supported document inside the documents folder.

    Supported formats:
    - .txt
    - .pdf

    Returns:
        List of dictionaries containing
        filename and text.
    """

    documents = []

    if not os.path.exists(folder_path):
        raise FileNotFoundError(
            f"Folder '{folder_path}' does not exist."
        )

    files = sorted(os.listdir(folder_path))

    for file_name in files:

        file_path = os.path.join(folder_path, file_name)

        # -----------------------------
        # Read TXT files
        # -----------------------------
        if file_name.lower().endswith(".txt"):

            text = read_txt(file_path)

        # -----------------------------
        # Read PDF files
        # -----------------------------
        elif file_name.lower().endswith(".pdf"):

            text = read_pdf(file_path)

        # -----------------------------
        # Skip unsupported files
        # -----------------------------
        else:
            continue

        if not text.strip():
            print(f"Skipping empty file: {file_name}")
            continue

        documents.append({
            "filename": file_name,
            "text": text
        })

    if len(documents) == 0:
        raise ValueError(
            "No valid documents (.txt or .pdf) found inside the documents folder."
        )

    return documents