import redis
from flask import Flask ,request
import json
from threading import Lock
lock = Lock()
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@app.route('/capsules/<string:name>')
def get_capsul_by_name(name: str):
       with open('./data.json') as data:
        input_dict= json.load(data)
        return list(filter(lambda x: x['name'] == name, input_dict))

@app.route('/capsules/<int:id>')
def get_capsul_by_id(id: int):
       with open('./data.json') as data:
        input_dict= json.load(data)
        return list(filter(lambda x: x['id'] == id, input_dict))

        # return str(id)

@app.route('/capsules/all')
def send_all_the_data():
       with open('./data.json') as data:
        return json.load(data)

@app.route('/image/<int:id>')
def get_image_by_id(id: int):
    with open('./data.json') as data:
     input_dict= json.load(data)
     return input_dict[[(idx) for idx, d in enumerate(input_dict) if d['id'] ==id][0]]["image"]

@app.route("/capsules/filterByProfile", methods=["POST"])
def filter_by_profile():
        profile = request.get_json()
        ans=[] 
        with open('./data.json') as data:
            input_dict= json.load(data)    
            for t in input_dict:
                  flag=True
                  for key, value in profile.items():
                    if(t["profile"].get(key)!=value):
                       flag=False
                  if(flag):
                   ans.append(t)        
        return ans

@app.route("/capsules/<int:id>/purchase", methods=["POST"])
def remove_from_stock(id: int):
    stock = request.get_json()
    lock.acquire()
    with open('./data.json','r+') as data:
       input_dict= json.load(data)
       input_dict[[(idx) for idx, d in enumerate(input_dict) if d['id'] ==id][0]]["Stocked"]-=stock["purchase"]
       data.seek(0)
       json.dump(input_dict, data, indent=4)
       data.close()
       lock.release()   
       return "true"

@app.route("/capsules/<int:id>/restock", methods=["POST"])
def add_to_stock(id: int):
    stock = request.get_json()
    lock.acquire()
    with open('./data.json','r+') as data:
       input_dict= json.load(data)
       input_dict[[(idx) for idx, d in enumerate(input_dict) if d['id'] ==id][0]]["Stocked"]+=stock["stock"]
       data.seek(0)
       json.dump(input_dict, data, indent=4)
       data.close()
       lock.release()   
       return "true"
    
@app.route("/capsules/<int:id>", methods=["PUT"])
def upfdate_capsule(id: int):
    newObj = request.get_json()
    lock.acquire()
    with open('./data.json','r+') as data:
       input_dict= json.load(data)
       index=next((i for i, obj in enumerate(input_dict) if obj['id'] == id), -1)
       if(index!=-1):
           if(newObj.get("profile")):
               input_dict[index]["profile"].update(newObj.get("profile"))
               profile= input_dict[index]["profile"]
               input_dict[index].update(newObj)
               input_dict[index]["profile"].update(profile) 
           input_dict[index].update(newObj)

       else:
           input_dict.append(newObj) 
       data.seek(0)
       json.dump(input_dict, data, indent=4)
       data.close()
       lock.release()   
       return "true"

   




