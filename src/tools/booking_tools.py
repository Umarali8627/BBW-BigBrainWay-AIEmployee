from langchain.tools import tool 
import json 




@tool 
def checkAvailiabilty() -> dict:
    """check the availiable slots in current week of the sales person and show to the user"""

    availible_slots = {'Monday':['10 am ', '12pm ','6pm'],
                       'Wednesday':['9am ', '4pm ','9pm'],
                       'Friday':['9am ', '4pm ','9pm'],
                       }

    return availible_slots

    


