import json
import requests


host = 'http://127.0.0.1:5005'
data = {
        'name':'Chris',
        'lastname':'Smalling'
}
response = requests.post(host+'/api/latest/usermanager/user/5',
                        data=json.dumps(data),
                        headers={'Content-Type': 'application/json'})
if response.status_code == 200:
    print('-'*15)
    print('test 1: create new user test passed')
    print('-'*15)

data = {
        'name':'Chris',
        'lastname':'Harry'
}
response = requests.put(host+'/api/latest/usermanager/user/5',
                        data=json.dumps(data),
                        headers={'Content-Type': 'application/json'})
if response.status_code == 200:
    print('-'*15)
    print('test 2: update existing user passed')
    print('-'*15)

response = requests.get(host+'/api/latest/usermanager/user/2')
if response.status_code == 400:
    print('-'*15)
    print('test 3: get non-existing user passed')
    print('-'*15)
