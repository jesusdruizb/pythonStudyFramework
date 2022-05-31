import requests
import json
import jsonpath


#URL
baseUrl = 'https://reqres.in'
resourceSingleUser = '/api/users/2'
urlSingleUser = baseUrl+resourceSingleUser


#Delete Operation
response = requests.delete(urlSingleUser)

print(response)

assert response.status_code == 204
