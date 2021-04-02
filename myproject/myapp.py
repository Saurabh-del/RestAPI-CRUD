# 3rd party application
# it can be any application whether android, web any language

import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

# -------------------Read-------------------


def get_data(id=None):
    data = {}

    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print('---------------------------')
    print(data)

#get_data(4)    


# ------------- Create Implemented -----------
# For Create functionality
# create method implemented in serializers.py then this function implemented

def post_data():
    data = {
        'name': 'Ravi2',
        'roll': 1042,
        'city': 'Delhi2'
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print('---------------------------')
    print(data)

#post_data()


# ---------------Update implemeted ------------------
# also update implemeted in serializers.py

def update_data():
    data = {
        'id': 2,
        'name': 'Saurabh2',
        'city': 'Mathura'
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print('---------------------------')
    print(data)

# Complete Update -- All data required from client side
# Partial Update -- All Data not required-- Patch

#update_data()


def delete_data():
    data = {'id' : 6}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print('---------------------------')
    print(data)

delete_data()

