'''

Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!


'''

import sys
import sqlalchemy
from sqlalchemy_utils import database_exists, create_database, drop_database
from pprint import pprint

def menu():
    print("***************Main Menu****************")
    print()
    choice = input("""
                        a: Select Student
                        b: Select Class
                        q: Quit
                        
                        Please Enter Your Choice: """)
    if choice == "a":
        select_student()
    elif choice == "b":
        select_class()
    elif choice =="q":
        sys.exit
    else:
        print("You are a numpty")
        menu()

def select_student():
    pass

def select_class():
    pass

# Create Database

engine = sqlalchemy.create_engine('postgresql://postgres:harry5@localhost:5432/ex4db')

if database_exists(engine.url):
    drop_database(engine.url)

create_database(engine.url)
print(database_exists(engine.url))

engine = sqlalchemy.create_engine('postgresql://postgres:harry5@localhost:5432/ex4db')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

# Create Tables

students = sqlalchemy.Table('students', metadata,
                            sqlalchemy.Column('id', sqlalchemy.Integer(), primary_key=True),
                            sqlalchemy.Column('student_name', sqlalchemy.String(255))
                            )

classes = sqlalchemy.Table('classes', metadata,
                            sqlalchemy.Column('id', sqlalchemy.Integer(), primary_key=True),
                            sqlalchemy.Column('class_name', sqlalchemy.String(255))
                            )

studentclasses = sqlalchemy.Table('student_classes', metadata,
                            sqlalchemy.Column('studentid', sqlalchemy.Integer(), sqlalchemy.ForeignKey("students.id")),
                            sqlalchemy.Column('classid', sqlalchemy.Integer(), sqlalchemy.ForeignKey("classes.id"))
                            )

metadata.create_all(engine)

# Insert Data

query_1 = sqlalchemy.insert(students)
new_student_records = [{'id':'1', 'student_name':'Bob'},
                       {'id':'2', 'student_name':'Sarah'},
                       {'id': '3', 'student_name': 'Harry'}]
result_proxy_1 = connection.execute(query_1, new_student_records)

query_2 = sqlalchemy.insert(classes)
new_class_records = [{'id':'1', 'class_name':'Chemistry'},
                       {'id':'2', 'class_name':'History'},
                       {'id': '3', 'class_name': 'English'}]
result_proxy_1 = connection.execute(query_2, new_class_records)

query_3 = sqlalchemy.insert(studentclasses)
new_studentclass_records = [{'studentid':'1', 'classid':'1'},
                       {'studentid':'2', 'classid':'1'},
                       {'studentid': '3', 'classid': '1'}]
result_proxy_1 = connection.execute(query_3, new_studentclass_records)

# Joins

join_1 = students.join(studentclasses, students.columns.id == studentclasses.columns.studentid)
join_2 = join_1.join(classes, studentclasses.columns.classid == classes.columns.id)

selection = str('History')
query4 = sqlalchemy.select([students]).where(classes.columns.class_name == selection )
result_proxy = connection.execute(query4)
result_set = result_proxy.fetchall()
pprint(result_set)
