import json


def from_json(json_string):
    try:
        result = json.loads(json_string)
    except json.JSONDecodeError:
        result = {}
    return {}


def to_json(dictionary):
    # TODO Проверка, что это действительно словарь
    return json.dumps(dictionary)
