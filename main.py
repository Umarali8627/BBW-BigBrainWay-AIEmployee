from fastapi import FastAPI
from src.rag_structure import rag_pipeline
from src.agents.rag_agent import agent
from src.agents import supervisor_agent
# from src.agents import lead_agent





app = FastAPI(
    title = "BBW AI Employee MultiAgent Assistant",
    description = "This is a multi-agent assistant that have subagents that can perform specific tasks.",
    version = "1.0.0",

)


@app.get("/")
def health_check():
    return {"message": "BBW AI Employee MultiAgent Assistant is running."}
@app.post('/chat')
def chat_with_rag(query:str)->str:
      return rag_pipeline.chat_with_rag(query)
