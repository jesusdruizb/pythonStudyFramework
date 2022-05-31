import requests
import json
import jsonpath

#First API test


#URL
baseUrl = 'https://reqres.in'
resourceSingleUser = '/api/users/2'
resourceAllUsers = '/api/users?page=2'
urlSingleUser = baseUrl+resourceSingleUser
urlAllUsers = baseUrl+resourceAllUsers

#Send GET Request

getSingleUserResponse = requests.get(urlSingleUser)
getAllUsersResponse = requests.get(urlAllUsers)

#Display Response Content
print(getSingleUserResponse.content)
print(getSingleUserResponse.headers)
print(getSingleUserResponse.headers.get('Date'))
print(getSingleUserResponse.headers.get('Content-Type'))
print(getSingleUserResponse.status_code)
assert getSingleUserResponse.status_code == 200

print(getAllUsersResponse.content)
print(getAllUsersResponse.headers)
print(getAllUsersResponse.headers.get('Date'))
print(getAllUsersResponse.headers.get('Content-Type'))
print(getAllUsersResponse.status_code)
assert getAllUsersResponse.status_code == 200

#find data using jsonPAth
jsonSingleUserResponse = json.loads(getSingleUserResponse.text)
singleUserData = jsonpath.jsonpath(jsonSingleUserResponse,'data.id')
print(singleUserData)

jsonAllUsersResponse = json.loads(getAllUsersResponse.text)
allUsersData = jsonpath.jsonpath(jsonAllUsersResponse,'data[3]')
print(allUsersData)

for i in range (0,3):
    first_name = jsonpath.jsonpath(jsonAllUsersResponse, f'data[{str(i)}].first_name')
    print(first_name[0])