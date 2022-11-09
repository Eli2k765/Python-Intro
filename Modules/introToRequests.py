#requests is a library that allows you to make HTTP requests
import requests
import numbers

url = "https://www.google.com"

#This is a GET request
r = requests.get(url)

#This is a POST request
#r = requests.post(url)

#This is a PUT request
#r = requests.put(url)

#This is a DELETE request
#r = requests.delete(url)

#We can get the status code of the request
print(r.status_code)

#We can get the headers of the request
print(r.headers)

#We can also get the cookies of the request
print(r.cookies)

#We can get the content of the request
print(r.content)

#We can get the text of the request
print(r.text)

#We can get the time it took to make the request
print(r.elapsed)

#We can pass parameters to the request
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=payload)
print(r.url)

#To give a header to the request
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r.headers)

#To give a cookie to the request
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.cookies)

#To give a body to the request
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post(url, data=payload)
print(r.text)

#To give a json to the request
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post(url, json=payload)
print(r.text)

#To give a file to the request
url = 'https://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
print(r.text)

#To give a auth to the request
from requests.auth import HTTPBasicAuth
r = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
print(r.text)

#We can also use a session to make requests
s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("https://httpbin.org/cookies")
print(r.text)
