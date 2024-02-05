from lib.age_checker import *

def test_access_granted():
   assert age_checker("2000-06-15") == "Access granted!"

def test_access_denied():
   assert age_checker("2020-06-15") == "Access Denied: You are 3 and the required age is 16 or over!"   
