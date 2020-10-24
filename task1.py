import requests
import sys
import task2 # Import second task for authorized requests option

def get_methods(response_json, all_methods, all_no_param, all_with_param):
    for key in response_json:
        value = None

        try:
            value = response_json[key]

            if type(value) is str:
                print(value)
                all_methods.append(value)
            
            else:
                continue

        except:
            continue

        if '{' in value:
            all_with_param.append(value)
        
        else:
            all_no_param.append(value)

            further_response = task2.auth_request(value)
                       
            if further_response.ok:
                try: 
                    get_methods(further_response.json(), all_methods, all_no_param, all_with_param)
                
                except ValueError:
                    continue 
           
if __name__ == "__main__":

    root_url = 'https://api.github.com'

    response = task2.auth_request(root_url)

    if response.status_code != 200:
        print("The provided url is not valid or another error occured")
        exit()

    all_possible = open('AllPossibleGitHubAPI.txt', 'w')
    no_param = open('AllPossibleGitHubAPI_noparameters.txt', 'w')
    with_param = open('AllPossibleGitHubAPI_requireparameters.txt', 'w')

    all_methods = []
    all_no_param = []
    all_with_param = []

    get_methods(response.json(), all_methods, all_no_param, all_with_param)

    all_possible.write('\n'.join(all_methods) + '\n')
    all_possible.close()

    no_param.write('\n'.join(all_no_param) + '\n')
    no_param.close()

    with_param.write('\n'.join(all_with_param) + '\n')
    with_param.close()
