'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
# Tested 27-08-19

import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:harry5@localhost:5432/dvdrental')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)

print(repr(metadata.tables['film']))
print(repr(metadata.tables['category']))
