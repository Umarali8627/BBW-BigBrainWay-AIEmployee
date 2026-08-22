from langchain.tools import tool 
from src.agents.rag_agent import agent 
from src.agents.lead_agent import lead_Agent
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