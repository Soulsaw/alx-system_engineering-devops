#!/usr/bin/python3
"""Don't import project"""
if __name__ == "__main__":
    """Import and implementation"""
    import csv
    import requests
    from sys import argv
    url = "https://jsonplaceholder.typicode.com/"
    user_id = int(argv[1])
    user = requests.get(url + "users/{}".format(user_id)).json()
    params = {'userId': user_id}
    todos = requests.get(url + "todos", params=params).json()
    with open(f"{user_id}.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([todo.get('userId'), user.get('username'),
                             todo.get('completed'), todo.get('title')])
        csvfile.close()
