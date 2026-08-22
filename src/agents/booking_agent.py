from langchain.agents import create_agent
from src.llm import model 
from src.tools import booking_tools


SYSTEM_PROMPT = """"""


booking_agent = create_agent(
    model=model.get_model(),
    tools = [],
    system_prompt=SYSTEM_PROMPT
)