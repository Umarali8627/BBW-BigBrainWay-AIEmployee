from langchain_community.document_loaders import TextLoader,PyPDFLoader
from typing import List 
from langchain_core.documents import Document
from pathlib import Path




def load_documents(file_path: str):
    """
    Load documents from a given file path.

    Args:
        file_path (str): The path to the file to be loaded."""
    
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents
def load_pdf_directory(directory: str) -> List[Document]:
    """
    Load all PDF documents from a directory.
    """

    documents = []

    pdf_files = Path(directory).glob("*.pdf")

    for pdf_file in pdf_files:
        print(f"Loading: {pdf_file}")

        loader = PyPDFLoader(str(pdf_file))

        pdf_documents = loader.load()

        documents.extend(pdf_documents)

    print(f"Loaded {len(documents)} pages.")

    return documents
