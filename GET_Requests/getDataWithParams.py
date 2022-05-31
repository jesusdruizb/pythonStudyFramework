import requests
import json
import jsonpath

#First API test


#URL
baseUrl = 'https://httpbin.org/get'

#PARAMS
params = {'name': 'getParamTest', 'email': 'getParamTest@fakemail.com', 'number': '0900-17288-88'}

#Send GET Request

getSingleUserResponse = requests.get(baseUrl,params)

#Display Response Content
print(getSingleUserResponse.text)
print(getSingleUserResponse.content)
print(getSingleUserResponse.headers)
print(getSingleUserResponse.status_code)