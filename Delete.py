from People import People
from Connection import Connection


def delete():
    connection = Connection("test", "People")
    collection = connection.getConnection()

    collection.remove({"phone": "5"})

delete()