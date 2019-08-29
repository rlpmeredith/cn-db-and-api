'''
Using sqlalchemy which the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of you choice comedy

- Select all the comedic films and that and sort them by rental rate

- Using one of the statements above, add a GROUP BY

- Using on of the statements above, add a ORDER BY

'''

import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:harry5@localhost:5432/dvdrental')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)

join_1 = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id)
join_2 = join_1.join(film, film.columns.film_id == film_actor.columns.film_id)

your_actor = str(input("Please enter the first names of the actor that you are interested in: "))
your_category = str(input("Please enter the film category that you are interested in: "))

query = sqlalchemy.select([actor]).where(actor.columns.first_name == your_actor.title() )
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
pprint(result_set)

query_2 = sqlalchemy.select([film.columns.title, actor.columns.first_name, actor.columns.last_name]).select_from(join_2).where(actor.columns.first_name == your_actor.title() )
result_proxy_2 = connection.execute(query_2)
result_set_2 = result_proxy_2.fetchall()
pprint(result_set_2)


