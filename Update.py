from People import People
from Connection import Connection


def update():
    connection = Connection("test", "People")
    collection = connection.getConnection()

    collection.update({"phone": "5"}, {"$set": {"name": "update"}}, upsert=False, multi=True)

update()