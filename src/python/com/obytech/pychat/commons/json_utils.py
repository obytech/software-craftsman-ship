import json
from collections import namedtuple


def json_to_object(data: str):
    # Parse JSON into an object with attributes corresponding to dict keys.
    return json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))