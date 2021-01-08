import requests
import json

url = 'http://127.0.0.1:8080/api/'

data = [4,64.6,0,0,32,1135.444444,0.002857143,0.00952381,0,0,'Feb',2,2,1,3,'Returning_Visitor',False]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)