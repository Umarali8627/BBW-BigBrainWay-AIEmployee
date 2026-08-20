from src.llm import model 
from langchain.agents import create_agent
from src.tools.supervisor_tools import knowledgeBase




SupervisorPrompt = """
You are a supervisor agent for BBW  AI Employee MultiAgent Assistant.
Use appropriate tool to answer the question use single or multitools for the sequence of tasks
Your role is to to classify the user intent into one of the following categories:
1.Knowledge Base : use Knowledge base tool to answert the question."""

supervisoragent = create_agent(
    model = model.get_model(),
    tools = [knowledgeBase],
    system_prompt=SupervisorPrompt
)

# test the supervisor tool 
query = "what services does BBW provides "
for step in supervisoragent.stream(
    {"messages":[{"role":"user","content":query}]}
):
    for update in step.values():
        for message in update.get("messages", []):
            message.pretty_print()


# query = "who is the cto of BBW?"

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