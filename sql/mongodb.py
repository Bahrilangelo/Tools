import pymongo

class MongoDB:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        self.client = pymongo.MongoClient(self.host, self.port)
        self.db = self.client['test']
        self.db.authenticate(self.username, self.password)

    def insert(self, data):
        self.db['test'].insert(data)

    def close(self):
        self.client.close()

# Inserting to the table

import json
import time
import random
def generate_random():
    return {
        'time': time.time(),
        'value': random.randint(0, 100)
    }
if __name__ == '__main__':
    # Connecting with database and inserting values into it in a loop for some number of times
    dbconn=MongoDB('localhost',27017,'admin','admin')   ##
    dbconn.connect()
    for i in range(100):
        dbconn.insert(generate_random())
    dbconn.close()

# Updating datas on the table

import json
import time
import random
def generate_random():
    return {
        'time': time.time(),
        'value': random.randint(0, 100)
    }
if __name__ == '__main__':
    # Connecting with database and inserting values into it in a loop for some number of times
    dbconn=MongoDB('localhost',27017,'admin','admin')   ##
    dbconn.connect()
    for i in range(100):
        dbconn.insert(generate_random())
    dbconn.close()
    import datetime as dt
    dbconn=MongoDB('localhost',27017,'admin','admin')   ##
    dbconn.connect()
    dbconn.db['test'].update({'time': {'$gt': time.time() - 60 * 60 * 24}}, {'$set': {'value': 0}}, multi=True)
    dbconn.close()

# Deleting datas on the table

import json
import time
import random
def generate_random():
    return {
        'time': time.time(),
        'value': random.randint(0, 100)
    }
if __name__ == '__main__':
    # Connecting with database and inserting values into it in a loop for some number of times
    dbconn=MongoDB('localhost',27017,'admin','admin')   ##
    dbconn.connect()
    for i in range(100):
        dbconn.insert(generate_random())
    dbconn.close()
    import datetime as dt
    dbconn=MongoDB('localhost',27017,'admin','admin')   ##
    dbconn.connect()
    dbconn.db['test'].remove({'time': {'$lt': time.time() - 60 * 60 * 24}})
    dbconn.close()

# Querying datas on the table
#using find method
# to query data from collection:
    # db.collection.find(query, projection)
# query is a dictionary specifying the query criteria
# projection is a dictionary specifying the fields to return
# if query is empty, all documents are returned
# if projection is empty, all fields are returned
# if both are empty, all documents and fields are returned
# if both are not empty, only documents matching the query criteria and only the specified fields are returned
# if projection is not empty, _id is not returned unless explicitly specified
# if projection is not empty, _id can be explicitly excluded by setting it to 0
# if projection is not empty, _id can be explicitly included by setting it to 1\
# if projection is not empty, all other fields are excluded unless explicitly included
# if projection is not empty, all other fields can be explicitly included by setting them to 1
# if projection is not empty, all other fields can be explicitly excluded by setting them to 0

import json
import time
import random
def generate_random():
    return {
        'time': time.time(),
        'value': random.randint(0, 100)
    }
if __name__ == '__main__':
    # Connecting with database and inserting values into it in a loop for some number of times
    dbconn=MongoDB('localhost',27017,'admin','admin')   ##
    dbconn.connect()
    for i in range(100):
        dbconn.insert(generate_random())
    dbconn.close()
    import datetime as dt
    dbconn=MongoDB('localhost',27017,'admin','admin')   ##
    dbconn.connect()
    for doc in dbconn.db['test'].find({'value': {'$gt': 50}}, {'_id': 0, 'value': 1}):
        print(doc)
    dbconn.close()
    