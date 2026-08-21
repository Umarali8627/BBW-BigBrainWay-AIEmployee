from src.llm import model 
from src.tools.lead_tools import collect_lead_data
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command




SYSTEM_PROMPT = """You are the Lead Qualification Agent for BBW . Use the collect_lead_data tool to collect the lead details"""

lead_Agent = create_agent(
    model = model.get_model(),
    tools = [collect_lead_data],
    system_prompt=SYSTEM_PROMPT,
    middleware=[HumanInTheLoopMiddleware(
        interrupt_on={
            "collect_lead_data":{
                "allowed_decisions":["approve","edit","reject"]
            }
        },
        description_prefix="Lead data pending review"
    )],
    checkpointer=InMemorySaver()
)

# test the lead agent 

# config = {'configurable':{'thread_id':'lead-123'}}
# query='hi ! i am looking for an ai chatbot'

# config = {"configurable": {"thread_id": "lead-conv-123"}}

# result = lead_Agent.invoke(
#     {"messages": [{"role": "user", "content": query}]},
#     config=config,
#     version="v2",
# )

# if result.interrupts:
#     print(f'INTERRUPT DETAIL : {result.interrupts[0]}')
#     action = result.interrupts[0].value["action_requests"][0]
#     print(action)
#     print(action["name"], action["args"])