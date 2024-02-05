from datetime import *
from dateutil.relativedelta import *


def age_checker(dob):
    dob = datetime.strptime(dob,"%Y-%m-%d") 
    today = date.today()
    age = relativedelta(today, dob).years 
    if age < 16:
        return "Access Denied: You are 3 and the required age is 16 or over!"
    else:
        return "Access granted!"
