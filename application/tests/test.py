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

data = {
        'name':'Chris',
        'lastname':'Harry'
}
response = requests.put(host+'/api/latest/usermanager/user/5',
                        data=json.dumps(data),
                        headers={'Content-Type': 'application/json'})
