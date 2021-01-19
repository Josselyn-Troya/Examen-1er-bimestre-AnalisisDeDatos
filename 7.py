import couchdb
import pymongo

couch_server=couchdb.Server()
couch_server.resource.credentials=('josselyn','josselyn')

couch_db = couch_server['facebook']

mongo_client= pymongo.MongoClient('mongodb+srv://examen:examen@cluster0.pwesb.mongodb.net/examen?retryWrites=true&w=majority')
mongo_client_db = mongo_client.get_database('examen')

for row in couch_db.view('_all_docs', include_docs=True):
    print(row['doc'])
    if mongo_client_db.udemy.count_documents({"_id":row['doc']['_id']})==0:
        mongo_client_db.udemy.insert(row['doc'])