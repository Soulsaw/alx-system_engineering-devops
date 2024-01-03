#!/usr/bin/python3
"""Don't import project"""
if __name__ == "__main__":
    """Import and implementation"""
    import json
    import requests
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/").json()
    new_dict = {}
    for user in users:
        params = {'userId': user.get('id')}
        todos = requests.get(url + "todos", params=params).json()
        new_dict[user.get('id')] = [{"username": user.get('username'),
                                     "task": todo.get('title'),
                                     "completed": todo.get('completed')
                                     } for todo in todos]
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(new_dict, jsonfile)
        jsonfile.close()
