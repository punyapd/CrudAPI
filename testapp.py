import requests
import json
URL = "http://127.0.0.1:8000/student_api/"
def getdata(id = None):
    data = { }
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url = URL , data = json_data)

    data = r.json()
    print(data)

#getdata()

def post_data():
    data = {
        'name':'kevin',
        'roll':'5',
        'address':'banepa',
        'age':'5',
        'contact':'44994003'
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL , data = json_data)
    data  = r.json()
    print(data)

#post_data()
def update_data():
    data = {
        'id' :'1',
        'name' : 'kevin',
        'address':'banepa',
        'age':'5',
        'contact':'44994003'
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL , data = json_data)
    data  = r.json()
    print(data)

#update_data()

def delete_data():
    data = {
        'id' :'1'}
    json_data = json.dumps(data)
    r = requests.delete(url = URL , data = json_data)
    data  = r.json()
    print(data)

delete_data()



