import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
#%%
###API ########################
ckey = "yHj6FBM2c02xhvA40qltScVi8"
csecret = "p74FwYmQrAZ4FLPvLg39q959CHsSpbFu6aE2NbRBge7qCby4px"
atoken = "1340168707704823808-wSnAAtdFmJ95tkFNXDUMZeXuhchxVL"
asecret = "730yQlP5ZFh797dakzluKuFlH50wCYE7Al21zQeseCddT"
#####################################
#%%
class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
#%% 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
#%%
'''========couchdb'=========='''
server = couchdb.Server('http://josselyn:josselyn@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('udemy')
except:
    db = server['udemy']
#%%   
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[-9.47,36.55,-0.54,42.4])  
twitterStream.filter(track=['Udemy'])

