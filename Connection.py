import pymongo

class Connection:
    
    def __init__(self, database, collection):
        self.database = database
        self.collection = collection
        self.url = "mongodb+srv://hugoroca:PWv0VINQIeSkMIeP@cluster0-xu1hg.mongodb.net/test"
        
    def getConnection(self):
        client = pymongo.MongoClient(self.url)
        
        db = client[self.database]
        
        return db[self.collection]