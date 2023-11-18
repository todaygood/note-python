import requests

"""
requests.get('http://httpbin.org/cookies/set/number/123456789')
response = requests.get('http://httpbin.org/cookies')
print(response.text)


s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
"""

response = requests.get('https://httpbin.org/basic-auth/user/pass',auth=('user','pass'))

print(response.status_code)

print(response.json())

