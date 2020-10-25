import requests
import sys
from os import path

url = 'https://api.github.com/user'
token = open('token', 'r').read().strip() if path.exists('token') else ''

def auth_request(url, token):
    headers = {'Authorization': 'token ' + token}

    return requests.get(url, headers=headers)

if __name__ == '__main__':
    status_code = auth_request(url, token).status_code

    print(f'Request returned response with status - {status_code} for token {token}')
