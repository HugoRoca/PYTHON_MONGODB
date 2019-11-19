from People import People
from Connection import Connection

def listMongodb():
    conection = Connection()
    
    modelPeopleList = [
        People("hugo1", "roca1", "24", "hugoroca@hotmail.com", "1"),
        People("hugo2", "roca2", "24", "hugoroca@hotmail.com", "2"),
        People("hugo3", "roca3", "24", "hugoroca@hotmail.com", "3"),
        People("hugo4", "roca4", "24", "hugoroca@hotmail.com", "4"),
        People("hugo5", "roca5", "24", "hugoroca@hotmail.com", "5")
    ]

    collection = conection.getConnection();

    for people in modelPeopleList:
        #print(people.toDbCollection())
        collection.insert(people.json())

listMongodb()