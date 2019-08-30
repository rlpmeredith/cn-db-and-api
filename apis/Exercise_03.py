'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

#Tested 26-08-19

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
body = {
    "first_name": "Bob",
    "last_name": "Meredith",
    "email": "afake@email.com"
}

response = requests.post(base_url, json=body)

print(response.status_code)

params = {
    "last_name": "Meredith"
}

response2 = requests.get(base_url, params=params)
print(response2.content)
