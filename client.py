"""
Client test module
"""
import requests
import json


# URL = 'http://localhost:5000/get_neighbors'

URL = 'http://ec2-3-67-94-128.eu-central-1.compute.amazonaws.com:8080/get_neighbors'

args = {'user_id': 654651351615,
        'user_zip': 'ITC86013',
        'basket': '[55, 1, 2, 3, 4, 5, 6, 7, 8, 9]',
        'n': 5
        }

r = requests.post(URL, json=args)

print(r.text)
