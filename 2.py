from bs4 import BeautifulSoup
import pandas as pd
import requests
import json
from pymongo import MongoClient
#%%
def find_2nd(string, substring):
    return string.find(substring, string.find(substring)+1)

def find_1st(string, substring):
    return string.find(substring, string.find(substring))
#%%
respose = requests.get('https://www.olx.com.ec/video-juegos-consolas_c802')
soup = BeautifulSoup(respose.content, 'lxml')
#%%
Product=[]
Price=[]
Location=[]
#%%
post_product = soup.find_all('span', class_='_2tW1I')
post_price = soup.find_all('span', class_='_89yzn')
post_location = soup.find_all('span', class_='tjgMj')
#%%
for element in post_product:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Product.append(limpio.strip())
#%%
for element in post_price:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Price.append(limpio.strip())
#%%
for element in post_location:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Location.append(limpio.strip())
#%%
dfDS=pd.DataFrame({'producto':Product,'precio':Price,'location':Location})
#%%
dfDS
#%%
db=[]
for i in range(0,len(Product)):
    data={'producto':Product[i],'precio':Price[i],'location':Location[i]}
    db.append(data)
#%%
myclient = MongoClient("mongodb://localhost:27017") 

try:
    mydb=myclient['web']
    mycol=mydb['olx']
except:
    mydb=myclient['web']
    mycol=mydb['olx']
    
#%%
doc={}
for i in range(len(dfDS)): 
    i= i+1
    try:
        doc['_id']=i

        doc['product']=dfDS.iloc[i,0]
        doc['price']=dfDS.iloc[i,1]
        doc['location']=dfDS.iloc[i,2]

        mycol.insert_one(doc)
        print(doc)
        print("guardado exitosamente")

    except Exception as e:    
            print("no se pudo grabar:" + str(e))

