import requests
import json

url = 'http://127.0.0.1:5000/site/'




data = [[4,64.6,0,0,32,1135.444444,0.002857143,0.00952381,0,0,2,2,2,1,3,2,0]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)