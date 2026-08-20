from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.document_loaders import (TextLoader
                                                  )





def chunk_documents(documents, chunk_size=1000, chunk_overlap=200) ->Document: 
    """
    Chunk the documents into smaller pieces.

    Args:
        documents (list): List of documents to be chunked.
        chunk_size (int): The size of each chunk.
        chunk_overlap (int): The overlap between chunks.

    Returns:
        list: List of chunked documents.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    
    chunkes = text_splitter.split_documents(documents)
   
    
    return chunkes
# test the chunking function
# if __name__ == "__main__":
#     file_path = "src/rag_structure/data/dummy_doc.txt"  
#     # Load documents
#     documents = load_documents(file_path)
    
#     # Chunk documents
#     chunked_docs = chunk_documents(documents, chunk_size=500, chunk_overlap=50)
#     print(f"Chunked {len(chunked_docs)} documents from {len(documents)} original documents.")
#     # Print the first 5 chunked documents
#     for i, doc in enumerate(chunked_docs[:5]):
#         print(f"Chunk {i}: {doc['content'][:200]}...")  

