from langchain.tools import tool 
from src.agents.rag_agent import agent 
from src.agents.lead_agent import lead_Agent
from src.agents.booking_agent import booking_agent
import json




@tool 
def knowledgeBase(request:str)->str:
     
    """
    Use this tool for questions about Big Brain Way (BBW),
    including its services, pricing, company information,
    offerings, and other information contained in the BBW
    knowledge base."""
    
    result=agent.invoke({
        'messages':[
            {
                'role':'user',
                'content':request
            }
        ]
    })
    return result['messages'][-1].content
config = {'congigurable':{'thread_id':'session-123'}}
@tool 
def lead_collector(request:str):
    """Use the lead collector tool to collect all the require detail of the lead 
    """
    result= lead_Agent.invoke({'messages':[{"role":'user','content':request}]},config= config)
    return result['messages'][-1].content
@tool 
def save_lead_data(lead_data: dict)-> str:
    """Use save lead data for storing the customer/lead data 
    """
    file_path= "src/tools/leads.json"
    with open(file_path,'r') as file :
        leads = json.load(file)
    # leads = []
    leads.append(lead_data)
    with open(file_path,"w",encoding='utf-8') as file:
        json.dump(leads,file,indent=4)


    return f"Data Saved successfully..."
@tool 
def manage_meetingtime(request:str)-> dict:
    """Use this tool to get the available slots for the meeting and then show the available options to select the time and day for the meeting"""
    result= booking_agent.invoke({'messages':[{"role":'user','content':request}]},config= config)
    return result['messages'][-1].content
@tool
def Book_client(lead_data:dict,meeting_time : dict) -> dict:
    """Use Book client when user select the time and day in available slot then book it """
    # lead_data['Booking_details'] = meeting_time
    booking_details =  {
        'lead_data': lead_data,
        'booking_details': meeting_time
    }
    print(booking_details)
    file_path= "src/tools/booking.json"
    with open(file_path,'r') as file :
            bookings = json.load(file)
    # bookings  = []
    bookings.append(booking_details)
    with open(file_path,"w",encoding='utf-8') as file:
            json.dump(bookings,file,indent=4)
        
    return f'Booking Confirmed'