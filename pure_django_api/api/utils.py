import json


def is_json(json_data):
    try:
        is_valid = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid