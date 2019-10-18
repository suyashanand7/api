from flask import Flask, request
from pymongo import MongoClient 
import json
app = Flask(__name__)
connect = MongoClient('mongo',27017)
db = connect['api_data']
collection1 = db["data"]
@app.route('/',methods=['GET','POST','PUT','DELETE'])
def data():
    if(request.method=='GET'):
        arr=[]
        for ab in collection1.find():
            arr.append(ab)
        return str(arr)
    if(request.method=='POST'):
        a = request.get_json()
        collection1.insert_one(a)
        return("POST DONE")
    if(request.method=='DELETE'):
        a = request.get_json()
        collection1.delete_one(a)
        return("DELETED")
    if(request.method=='PUT'):
        a = request.get_json()
        b = a[0]
        c = a[1]
        collection1.update_one(b,{"$set":c})
        return("UPDATED")
app.run(port=5000,host="0.0.0.0")