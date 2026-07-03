import os


def load_documents(folder_path):
    """
    Loads every .txt file inside the documents folder.

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

        if not file_name.endswith(".txt"):
            continue

        file_path = os.path.join(folder_path, file_name)

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        if not text.strip():
            print(f"Skipping empty file: {file_name}")
            continue

        documents.append({
            "filename": file_name,
            "text": text
        })

    if len(documents) == 0:
        raise ValueError(
            "No valid text documents found inside the documents folder."
        )

    return documents