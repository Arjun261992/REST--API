import requests
import json
URL = "https://127.0.0.1:8000/employeesapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data= {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.get(url= URL, headers=headers, data= json_data)
    data= r.json()
    print(data)

get_data(2)

def post_data():
    data= {
        'first_name': 'Sumit',
        'last_name': 'Rawat',
        'email': 'rawat@gmail.com',
        'phone': '80098076786'
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url= URL, headers=headers, data= json_data)
    data= r.json()
    print(data)
#post_data()

def delete_data():
    data = {'id': 5}
    json_data = json.dumps(data)
    r = requests.delete(url= URL, headers=headers, data= json_data)
    data= r.json()
    print(data)
#delete_data()