from langchain.agents import create_agent
from src.llm import model 
from src.tools.booking_tools import checkAvailiabilty


SYSTEM_PROMPT = """You are the Booking Agent that books client for the BBW Your main goal is to book a client in a available slots
use the checkAvailiblity to get the available slots for the meeting ."""


booking_agent = create_agent(
    model=model.get_model(),
    tools = [checkAvailiabilty],
    system_prompt=SYSTEM_PROMPT,
)
# config ={'configurable':{'thread_id':'u12'}}

# def testbookingagent():
#    while True:
#            query = input("User : ")
   
#            if query.lower() in ["exit", "quit"]:
#                print("Good Bye!")
#                break
   
#            stream = booking_agent.stream_events(
#                {
#                    "messages": [
#                        {
#                            "role": "user",
#                            "content": query
#                        }
#                    ]
#                },
#                version="v3",
#                config=config
#            )
   
#            for kind, item in stream.interleave("messages", "tool_calls"):
#                if kind == "messages":
#                    for token in item.text:
#                        print(token, end="", flush=True)
   
#                elif kind == "tool_calls":
#                    print(
#                        f"\nTool call: {item.tool_name}({item.input})"
#                    )
#                    print(
#                        f"Tool result: {item.output}"
#                    )
   
#            print()

# testbookingagent()