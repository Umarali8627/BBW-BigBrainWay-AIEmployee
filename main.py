from fastapi import FastAPI
from src.agents.supervisor_agent import chat
import uuid 
from src.tools.lead_tools import load_allleads
from src.tools.booking_tools import load_allbookings

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
@app.get('/leads')
def get_all_leads()->list:
    """get all the leads from the database and return as a list of json"""
    return load_allleads()

@app.get('/bookings')
def get_all_bookings()->list:
    """get all the bookings from the database and return as a list of json"""
    return load_allbookings()