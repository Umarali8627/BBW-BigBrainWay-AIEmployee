from langchain.tools import tool 
import json


@tool 
def collect_leadData(name : str,
                     email:str,
                     project_title:str,
                     budget:int) -> dict :
    """
    Use collect_leadData for collecting the require detail from the user and make sure to collect all the required field.
    If any field is remining so make sure to take all the data. """
    lead_deatil = {
            "Name":name,
            "Email":email,
            "Project":project_title,
            "budget":budget
        }
    return lead_deatil

