import requests
import json
import jsonpath

#URL
baseUrl = 'https://reqres.in'
resourceUpdateUser = '/api/users/2'
urlSingleUser = baseUrl+resourceUpdateUser

#read create user body json from file

file = open('../fixtures/updateUser.json','r')
json_input = file.read()
updateUserBodyFromFile = json.loads(json_input)

#PUT operation

response = requests.put(urlSingleUser, updateUserBodyFromFile)

print(response.content)
print(response.headers)
print(f'response code: {response.status_code}')

#Validating response
assert response.status_code == 200

#Parse response to JSON format

response_json = json.loads(response.text)

#check ID using jsonpath

print(jsonpath.jsonpath(response_json,'updatedAt'))

test = f'''{response_json}'''

print (test)