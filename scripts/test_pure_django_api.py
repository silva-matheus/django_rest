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

def create_update():
    new_data = {
        'user': 1,
        'content': 'update 4',
        'image': ''
    }

    r = requests.post("{}{}".format(BASE_URL, POST_ENDPOINT), data=new_data)
    print(r.status_code)
    # print(r.json())

print(get_list())
print(retrieve_record(2))
create_update()