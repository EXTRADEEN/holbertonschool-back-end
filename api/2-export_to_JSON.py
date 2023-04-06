#!/usr/bin/python3
"""
   script to export data in the JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    response_users = requests.get('https://jsonplaceholder.typicode.com/users')
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    employees = response_users.json()
    todos = response_todos.json()

    id = int(argv[1])

    for i in employees:
        if id == i.get('id'):
            username = i.get('username')
    joker = []
    for i in todos:
        harley_quin = {}
        if id == i.get('userId'):
           harley_quin['task'] = i.get('title')
           harley_quin['completed'] = i.get('completed')
           harley_quin['username'] = username
           joker.append(harley_quin)
    wonder_woman = {}
    wonder_woman[id] = joker

    with open(str(argv[1]) + ".json", "w") as USER_ID:
        json.dump(wonder_woman, USER_ID)
