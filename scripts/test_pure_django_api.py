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
        'content': 'update 5'
    }

    # r = requests.post("{}{}".format(BASE_URL, LIST_ENDPOINT), data=new_data)
    # r = requests.put("{}{}{}".format(BASE_URL, GET_ENDPOINT, id), json.dumps(new_data))
    r = requests.delete("{}{}{}".format(BASE_URL, GET_ENDPOINT, id))
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.status_code
    

print(get_list())
print(create_update(3))