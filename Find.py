import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://hugoroca:PWv0VINQIeSkMIeP@cluster0-xu1hg.mongodb.net/test")

db = client.test

collection = db.People

cursor = collection.find()

for people in cursor:
    print (people['name'] + ' - ' + people['lastname'] + ' - ' + people['age'] + ' - ' + people['email'] + ' - ' + people['phone'])