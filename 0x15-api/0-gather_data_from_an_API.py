#!/usr/bin/python3
"""Import modules"""
if __name__ == "__main__":
    import requests
    from sys import argv
    idUser = argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{idUser}/todos"
    url1 = f"https://jsonplaceholder.typicode.com/users/{idUser}"
    with requests.get(url1) as response:
        json = response.json()
        EMPLOYEE_NAME = json['name']
    with requests.get(url) as response:
        json = response.json()
        TOTAL_NUMBER_OF_TASKS = len(json)
        NUMBER_OF_DONE_TASKS = len([x for x in json if x['completed']])
        print("Employee {} is done with tasks({}/{}):".format(
            EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
        [print('\t', x['title']) for x in json if x['completed']]
