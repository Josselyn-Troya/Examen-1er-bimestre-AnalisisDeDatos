import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
#%%
try:
    client = MongoClient('localhost')
    print (client.list_database_names())
    clientatl = MongoClient('mongodb+srv://examen:examen@cluster0.pwesb.mongodb.net/examen?retryWrites=true&w=majority')
    print (clientatl.list_database_names())
except requests.ConnectionError as e:
    raise e

db = client['twitter']
col = db['udemy']
dbatl = clientatl['examen']
colatl = dbatl['udemy']

for doc in col.find({}):
    print(doc)
    

for doc in col.find({}):
    colatl.insert_one(doc)
    print(doc)

for doc in colatl.find({}):
    print(doc)
