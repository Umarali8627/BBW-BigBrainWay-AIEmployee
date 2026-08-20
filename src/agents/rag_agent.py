from src.rag_structure.rag_pipeline import rag_retriever_tool
from langchain.agents import create_agent
from src.llm import model 




SYSTEM_PROMPT = """
You are a helpful AI assistant for BBW (Big Brain Way).

You answer questions about BBW using the BBW knowledge base.

Rules:
1. Use the rag_retriever_tool when the question requires information about BBW.
2. Do not invent information.
3. If the information is not available in the retrieved documents, say:
   "I don't know based on the available information."
4. Keep answers concise and useful.
"""

agent  = create_agent(
    model = model.get_model(),
    tools = [rag_retriever_tool],
    system_prompt=SYSTEM_PROMPT,

)
# test the rag agent 
# response = agent.invoke({
#     'messages':[ {
#         'role':'user',
#         'content':'which services does BBW Provides'
#         }
#     ]
# })
# print(response['messages'][-1].content)