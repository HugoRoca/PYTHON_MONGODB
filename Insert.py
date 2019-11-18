import pymongo
from People import People

modelPeopleList = [
    People("hugo1", "roca1", "24", "hugoroca@hotmail.com", "1"),
    People("hugo2", "roca2", "24", "hugoroca@hotmail.com", "2"),
    People("hugo3", "roca3", "24", "hugoroca@hotmail.com", "3"),
    People("hugo4", "roca4", "24", "hugoroca@hotmail.com", "4"),
    People("hugo5", "roca5", "24", "hugoroca@hotmail.com", "5")
]

client = pymongo.MongoClient(
    "mongodb+srv://hugoroca:PWv0VINQIeSkMIeP@cluster0-xu1hg.mongodb.net/test")

db = client.test

collection = db.People

for people in modelPeopleList:
    #print(people.toDbCollection())
    collection.insert(people.json())
