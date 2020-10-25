import requests
import sys

url = 'https://api.github.com/user'
token = open('token', 'r').read().strip()

def auth_request(url):
    global token 

    headers = {'Authorization': 'token ' + token}

    return requests.get(url, headers=headers)

if __name__ == '__main__':
    status_code = auth_request(url).status_code

    print(f'Request returned response with status - {status_code} for token {token}')
