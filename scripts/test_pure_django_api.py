import requests
import json

BASE_URL = "http://127.0.0.1:8000/"

LIST_ENDPOINT = "api/list"

GET_ENDPOINT = "api/get/"

POST_ENDPOINT = "api/post/"

def get_list():
    r = requests.get("{}{}".format(BASE_URL, LIST_ENDPOINT))
    return json.dumps(r.json())

def retrieve_record(id):
    r = requests.get("{}{}{}".format(BASE_URL, GET_ENDPOINT, id))
    return json.dumps(r.json())

def create_update(id):
    new_data = {
        'user': 1,
        'content': 'update 5',
        'image': ''
    }

    # r = requests.post("{}{}".format(BASE_URL, LIST_ENDPOINT), data=new_data)
    r = requests.put("{}{}{}".format(BASE_URL, GET_ENDPOINT, id), data=new_data)#json.dumps(new_data))
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.status_code
    
    # print(r.json())

# print(get_list())
print(retrieve_record(2))
print(create_update(1))