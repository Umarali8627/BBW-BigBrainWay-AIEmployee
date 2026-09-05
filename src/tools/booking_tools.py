from langchain.tools import tool 
import json 




@tool 
def checkAvailiabilty() -> dict:
    """check the availiable slots in current week of the sales person calendar  and show the available options to the user """
    # come from calendar of the sales person and show to the user
    availible_slots = {
        'Monday':['10 am ', '12pm ','6pm'],
        'Wednesday':['9am ', '4pm ','9pm'],
        'Friday':['9am ', '4pm ','9pm'],
                       }

    return availible_slots

    

def load_allbookings()-> list: 
    """load all the bookings from the database and return as a list of json"""
    # come from file and return as a list of json
    with open('src/tools/booking.json', 'r') as f:
        bookings = json.load(f)
    return bookings


# print(load_allbookings())
