import requests
import sys

url = 'https://api.github.com/'
username = 'simaz33'
token = open('token', 'r').read().strip()

def auth_request(url):
    global username, token

    if len(sys.argv) > 1:
        token = sys.argv[1]

    return requests.get(url, auth=(username, token))

if __name__ == '__main__':
    if auth_request(url).status_code == 200:
        print(f'Request returned response with status - 200 for user {username} and token {token}')
