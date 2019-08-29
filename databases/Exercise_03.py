'''
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

'''
# Tested 29-08-2019

import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:harry5@localhost:5432/dvdrental')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.update(film).values(rental_duration=10).where(film.columns.length > 150)

result = connection.execute(query)