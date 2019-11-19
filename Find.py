from People import People
from Connection import Connection

def Find():
    conection = Connection("test", "People")
    
    collection = conection.getConnection()

    cursor = collection.find()

    for people in cursor:
        print (people['name'] + ' - ' + people['lastname'] + ' - ' + people['age'] + ' - ' + people['email'] + ' - ' + people['phone'])
        
Find()