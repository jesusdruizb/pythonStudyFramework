import requests
import json
import jsonpath

#URL
baseUrl = 'https://reqres.in'
resourceCreateUser = '/api/users'
urlSingleUser = baseUrl+resourceCreateUser
body = ''''{
    "name": "Neo",
    "job": "Chosen"
}'''

#read create user body json from file

file = open('../fixtures/createUserBody.json','r')
json_input = file.read()
createUserBodyFromFile = json.loads(json_input)

#POST operation

response = requests.post(urlSingleUser, createUserBodyFromFile)

print(response.content)
print(response.headers)
print(response.headers.get('Content-Length'))
print(f'response code: {response.status_code}')

#Validating response
assert response.status_code == 201

#Parse response to JSON format

response_json = json.loads(response.text)

#check ID using jsonpath
print(jsonpath.jsonpath(response_json,'id'))

