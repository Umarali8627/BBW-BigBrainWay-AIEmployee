from langchain.tools import tool 



@tool 
def collect_lead_data(name:str,email:str,project_title:str,budget:int)-> dict:
    """Use collect lead data for collecting the customer/lead data make sure to take all the 
    required fields name ,email,projecttitle,budget"""
    lead_deatil = {
        "Name":name,
        "Email":email,
        "Project":project_title,
        "budget":budget
    }
    # the detail is store in the CRM later
    # save_to_crm(lead_deatil)

    return lead_deatil
