"""
Client test module
"""
import requests

URL = 'http://ec2-3-67-94-128.eu-central-1.compute.amazonaws.com:8080/get_neighbors'

body = {'user_id': 1000,
        'user_zip': 'ITC86013',
        'basket': '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'
        }

r = requests.get(URL, body)

print(r.text)
