import requests
import sys
import task2
from os import path
from git import Repo # git module was used for cloning repositories into local system

token = task2.token

def clone_repo(repo_url, repo_name):
    if not path.exists(repo_name):
        Repo.clone_from(repo_url, repo_name)
        print(f'Cloned {repo_url} -> {repo_name}')
    else:
        print(f'A directory with name \'{repo_name}\' already exists, canceling cloning')

def list_user_repos(username):
    page = 1

    while True:
        repo_url = f'https://api.github.com/users/{username}/repos?page={page}'
        repos_in_page = task2.auth_request(repo_url, token).json()
        
        if repos_in_page:
            for repo in repos_in_page:
                if type(repo) == dict:
                    print(repo['name'])
        else:
            break

        page += 1

if __name__ == '__main__':
    args = len(sys.argv)
    repo_name = ''
    repo_url = ''

    if args < 2:
        print('Not enough arguments specified: task4.py <user> [repo_name]')
        exit()

    elif args == 2:
        username = sys.argv[1].strip()
        list_user_repos(username)

        repo_name = input('Type name of the repo you want to clone: ').strip()
        repo_url = f'https://github.com/{username}/{repo_name}'

    elif args >= 3:
        username = sys.argv[1].strip()
        repo_name = sys.argv[2].strip()

        repo_url = f'https://github.com/{username}/{repo_name}'

    if task2.auth_request(repo_url, token).status_code == 200:
        if repo_url and repo_name:
            clone_repo(repo_url, repo_name)
        else:
            print(f'Could not locate such repo {repo_url}')
    else:
        print(f'User {username} does not have such repo \'{repo_name}\'')
