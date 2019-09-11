'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''

import requests
from pprint import pprint

base_url_users = "http://demo.codingnomads.co:8080/tasks_api/users"
user_response = requests.get(base_url_users)
initial_user_dict = user_response.json()

base_url_tasks = "http://demo.codingnomads.co:8080/tasks_api/tasks"
task_response = requests.get(base_url_tasks)
initial_task_dict = task_response.json()

user_list = []
for my_user in initial_user_dict["data"]:
    if my_user["first_name"] != "[YOUR FIRST NAME FIELD]":
        user_item = []
        for item in my_user:
            user_item.append(my_user[item])
    user_list.append(user_item)


task_list = []
for my_task in initial_task_dict["data"]:
    task_item = []
    for item in my_task:
        task_item.append(my_task[item])
    task_list.append(task_item)

print(user_list)
print(task_list)


