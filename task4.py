import requests
import task2

user = 'simaz33'
repo_name = 'dotnet'

page = 1


while True:
    repo_url = f'https://api.github.com/users/{user}/repos?page={page}'
    repos_in_page = task2.auth_request(repo_url).json()
    
    if repos_in_page:
        for repo in repos_in_page:
            print(repo['name'])

        page += 1

    else:
        break
