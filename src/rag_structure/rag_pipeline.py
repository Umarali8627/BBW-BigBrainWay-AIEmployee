from src.llm.model import get_model
from src.rag_structure.reteriver import HybridRetriever
from src.rag_structure.chunker import  chunk_documents
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableParallel,RunnableLambda
from src.rag_structure.document_loader import load_documents,load_pdf_directory
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent
from langchain.tools import tool


dir_path = "src/rag_structure/data"
documents = load_pdf_directory(dir_path)

# Chunk documents
chunked_documents = chunk_documents(documents, chunk_size=500, chunk_overlap=50)

# Initialize the retriever
retriever = HybridRetriever(documents=chunked_documents, bm25_weight=0.5, k=4)

model  = get_model()

PROMPT = ChatPromptTemplate.from_template("""
You are a helpful AI assistant for BBW (Big Brain Way).

Answer the user's question using ONLY the context provided below.

Rules:
1. Do not invent information.
2. If the answer is present in the context, answer clearly.
3. If the answer is not present in the context, say:
   "I don't know based on the available information."
4. Keep the answer concise and useful.

Context:
{context}

Question:
{query}
"""
                                          )

                                          
def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])
rag_chain = (
    {
        "context": RunnableLambda(retriever.search) | format_docs,
        "query": RunnablePassthrough()
    }
    | PROMPT
    | model
    | StrOutputParser()
)

def chat_with_rag(query:str)->str:
    """Chat with RAG (Retriever-Augmented Generation) model."""
    response = rag_chain.invoke(query)
    return response


# create retreiver as a tool 
@tool 
def rag_retriever_tool(query:str)->str:
    """Tool to retrieve relevant documents for the BBW official data  based on the query."""
    docs = retriever.search(query)
    return format_docs(docs)

