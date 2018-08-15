"""
Holds development speed bump removers
"""
from collections import OrderedDict
from ..wrappers import LookupDict
from flask import g
import json


def get_json_request(method=None, payload=None, ip="localhost:0.0.0.0:8000"):
    dummy = LookupDict()
    dummy.mimetype = "application/json"
    dummy.access_route = ip
    dummy.method = method or "post"
    dummy.json = payload
    dummy.headers = {
        "Content-Type": dummy.mimetype,
        "Authorization": "woidskldjskljalkdjalkdjkladjsldkajdkljadkl"
    }
    g.resolved_token = dummy.headers
    return dummy


def get_user_id():
    user_details = g.resolved_token.get('data', None)
    if user_details:
        if not isinstance(user_details, dict):
            user_details_dict = json.loads(user_details)
            user = user_details_dict['user_id']
        else:
            user = user_details['user_id']

        return user

    else:
        user = g.resolved_token['user_id']
        return user
