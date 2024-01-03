#!/usr/bin/python3
"""Don't import project"""
if __name__ == "__main__":
    """Import and implementation"""
    import json
    import requests
    from sys import argv
    url = "https://jsonplaceholder.typicode.com/"
    user_id = int(argv[1])
    user = requests.get(url + "users/{}".format(user_id)).json()
    params = {'userId': user_id}
    todos = requests.get(url + "todos", params=params).json()
    new_dict = {}
    new_dict[user.get('id')] = [{"task": todo.get('title'),
                                 "completed": todo.get('completed'),
                                 "username": user.get('username')
                                 } for todo in todos]
    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(new_dict, jsonfile)
        jsonfile.close()
