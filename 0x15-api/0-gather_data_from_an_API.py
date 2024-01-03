#!/usr/bin/python3
"""Import modules"""
if __name__ == "__main__":
    import requests
    from sys import argv
    idUser = argv[1]
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    id = int(argv[1])
    users = requests.get(users_url).json()
    for user in users:
        if user['id'] == id:
            name = user['name']
            break
    todos = requests.get(todos_url).json()
    task_total = [todo for todo in todos if todo['userId'] == id]
    task_completed = [todo for todo in todos if todo['completed']
                      and todo['userId'] == id]
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(task_completed), len(task_total)))
    [print('\t', x['title']) for x in task_completed]
