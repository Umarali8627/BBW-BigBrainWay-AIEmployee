from fastapi import FastAPI
from src.rag_structure import rag_pipeline
from src.agents.rag_agent import agent
from src.agents.supervisor_agent import chat
from src.agents import lead_agent
import uuid 
from src.agents import booking_agent

session_id = (uuid.uuid4())



app = FastAPI(
    title = "BBW AI Employee MultiAgent Assistant",
    description = "This is a multi-agent assistant that have subagents that can perform specific tasks.",
    version = "1.0.0",

)


@app.get("/")
def health_check():
    return {"message": "BBW AI Employee MultiAgent Assistant is running."}
@app.post('/chat')
def chat_with_Supervisor(query:str)->str:
     
      return chat(query,session_id)
