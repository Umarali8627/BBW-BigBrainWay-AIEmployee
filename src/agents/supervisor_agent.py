from src.llm import model 
from langchain.agents import create_agent
from src.tools.supervisor_tools import knowledgeBase,lead_collector,save_lead_data,Book_client
from langgraph.checkpoint.memory import InMemorySaver




SupervisorPrompt = """
You are a supervisor agent for BBW  AI Employee MultiAgent Assistant.
Use appropriate tool to answer the question use single or multitools for the sequence of tasks
Your role is to to classify the user intent into one of the following categories:
1.Knowledge Base : use Knowledge base tool to answert the question.
2.lead collector : Use this tool whenever a user have intent of the building something or to be our customer.to collect the lead data.
3.save_lead_data:Use this tool to save the current lead data and make sure to save the data after collecting lead data.
4.Book_client: use this tool to book a client for a meeting after collecting the lead data and selecting an available time slot."""

supervisoragent = create_agent(
    model = model.get_model(),
    tools = [knowledgeBase,lead_collector,save_lead_data,Book_client],
    system_prompt=SupervisorPrompt,
    checkpointer=InMemorySaver()

)

# test the supervisor tool 
# query = "i want to create a chatbot for my dental clinic?"
# for step in supervisoragent.stream(
#     {"messages":[{"role":"user","content":query}]}
# ):
#     for update in step.values():
#         for message in update.get("messages", []):
#             message.pretty_print()
# result = supervisoragent.invoke({'messages':[{'role':'user','content':query}]})

# if result.interrupts:
#     print(f'INTERRUPT DETAIL : {result.interrupts[0]}')
#     action = result.interrupts[0].value["action_requests"][0]
#     print(action)
#     print(action["name"], action["args"])
# # else :
#     print(result['messages'][-1].content)

config = {'configurable':{'thread_id':'thread-123'}}

def test_supervisor():
    while True:
        query = input("User : ")

        if query.lower() in ["exit", "quit"]:
            print("Good Bye!")
            break

        stream = supervisoragent.stream_events(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            },
            version="v3",
            config=config
        )

        for kind, item in stream.interleave("messages", "tool_calls"):
            if kind == "messages":
                for token in item.text:
                    print(token, end="", flush=True)

            elif kind == "tool_calls":
                print(
                    f"\nTool call: {item.tool_name}({item.input})"
                )
                print(
                    f"Tool result: {item.output}"
                )

        print()
test_supervisor()

def chat(request:str,session_id: str):
    """Chat with supervisor Agent that handles all kind of application tasks"""
    # creating config for the current uuid 
    config = {'configurable':{'thread_id':session_id}}
    response = supervisoragent.invoke({'messages':[{'role':'user','content':request}]},config = config)
    return response['messages'][-1].content