from src.llm import model 
from langchain.agents import create_agent
from src.tools.supervisor_tools import knowledgeBase,lead_collector




SupervisorPrompt = """
You are a supervisor agent for BBW  AI Employee MultiAgent Assistant.
Use appropriate tool to answer the question use single or multitools for the sequence of tasks
Your role is to to classify the user intent into one of the following categories:
1.Knowledge Base : use Knowledge base tool to answert the question.
2.lead collector: Use this tool whenever a user have intent of the sales.to collect the lead data"""

supervisoragent = create_agent(
    model = model.get_model(),
    tools = [knowledgeBase,lead_collector],
    system_prompt=SupervisorPrompt
)

# test the supervisor tool 
query = "i want to create a chatbot for my dental clinic?"
# for step in supervisoragent.stream(
#     {"messages":[{"role":"user","content":query}]}
# ):
#     for update in step.values():
#         for message in update.get("messages", []):
#             message.pretty_print()
result = supervisoragent.invoke({'messages':[{'role':'user','content':query}]})

if result.interrupts:
    print(f'INTERRUPT DETAIL : {result.interrupts[0]}')
    action = result.interrupts[0].value["action_requests"][0]
    print(action)
    print(action["name"], action["args"])
else :
    print(result['messages'][-1].content)

# stream = supervisoragent.stream_events(
#     {"messages": [{"role": "user", "content": query}]},
#     version="v3",
# )
# for kind, item in stream.interleave("messages", "tool_calls"):
#     if kind == "messages":
#         for token in item.text:
#             print(token, end="", flush=True)
#     elif kind == "tool_calls":
#         print(f"\nTool call: {item.tool_name}({item.input})")
#         print(f"Tool result: {item.output}")