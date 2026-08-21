from langchain.tools import tool 
from src.agents.rag_agent import agent 
from src.agents.lead_agent import lead_Agent




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
@tool 
def lead_collector(request:str):
    """Use the lead collector tool to collect all the require detail of the lead 
    """
    result= lead_Agent.invoke({'messages':[{"role":'user','content':request}]})
    return result['messages'][-1].content