from langchain.tools import tool 
from src.agents.rag_agent import agent 




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

