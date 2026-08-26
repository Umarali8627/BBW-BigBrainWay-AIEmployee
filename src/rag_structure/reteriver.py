

"""
Hybrid Search for production ready using vector and BM25
   retreiver with ensemble retrevier ,Using Class and method
"""
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever
from langchain_core .documents import Document
from typing import List
from langchain_openai import OpenAIEmbeddings
from src.utils.settings import settings



class HybridRetriever:
    """Production hybrid retriever with BM25 + vector search"""

    def __init__(self,documents:List[Document],bm25_weight:float=0.5,k:int = 4):
        self.k=k
        self.bm25_weight = bm25_weight
        self.vector_weight = 1- bm25_weight

        # Intialize embeddings 
        self.embeddigns = OpenAIEmbeddings(
            model="sentence-transformers/multi-qa-mpnet-base-dot-v1",   # any embedding model OpenRouter lists
            api_key=settings.OPEN_ROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
            check_embedding_ctx_length=False,
)
        # create vector store and retriever 
        self.vector_store = Chroma.from_documents(
            documents=documents,
            embedding= self.embeddigns,
            collection_name='hybrid_search',
            persist_directory='src/rag_structure/data/chroma_db'
        )
        self.vector_retreiver = self.vector_store.as_retriever(
            search_kwargs={'k':k}
        )
        # create BM25 retriever 
        self.bm25_retreiver = BM25Retriever.from_documents(documents,k=k)

        self.ensemble = EnsembleRetriever(
            retrievers=[self.bm25_retreiver,self.vector_retreiver],
            weights=[self.bm25_weight,self.vector_weight]
        )
    def search(self,query:str)->List[Document]:
        """Using Hybrid search Using EnsembleRetreiver (weight RRF)"""
        
        return self.ensemble.invoke(query)
    def add_documents(self,documents:List[Document]):
        """Add new documents to both retreivers"""
        # Add to vector store 
        self.vector_store.add_documents(documents)
        # Recreate BM25 (it dosen't support increamental adds)
        all_docs = self.vector_store.get()
        self.bm25_retreiver = BM25Retriever.from_documents(
            [Document(page_content=doc) for doc in all_docs['documents']],
            k=self.k
        )
