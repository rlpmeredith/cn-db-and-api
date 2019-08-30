'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

#Tested 26-08-19

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)
my_dict = response.json()

for my_user in my_dict["data"]:
    print(my_user["first_name"], my_user["last_name"], my_user["email"])
