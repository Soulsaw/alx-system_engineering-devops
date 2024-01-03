#!/usr/bin/python3
"""Don't import project"""
if __name__ == "__main__":
    """Import and implementation"""
    import requests
    from sys import argv
    url = "https://jsonplaceholder.typicode.com/"
    user_id = int(argv[1])
    user = requests.get(url + "users/{}".format(user_id)).json()
    params = {'userId': user_id}
    todos = requests.get(url + "todos", params=params).json()
    task_completed = [todo.get('title') for todo in todos
                      if todo.get('completed')]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(task_completed), len(todos)))
    [print('\t', x) for x in task_completed]
