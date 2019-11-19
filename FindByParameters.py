from People import People
from Connection import Connection

def FindByParameters():
    connection = Connection("test", "People")
    
    collection = connection.getConnection()
    
    cursor = collection.find({"phone":"5"})
    
    for people in cursor:
        print (people['name'] + ' - ' + people['lastname'] + ' - ' + people['age'] + ' - ' + people['email'] + ' - ' + people['phone'])
    
FindByParameters()