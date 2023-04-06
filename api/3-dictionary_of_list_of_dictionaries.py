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
    wonder_woman = {}
    for j in employees:
        user_id = j.get('id')
        username = j.get('username')
        joker = []
        for i in todos:
            harley_quin = {}
            if user_id == i.get('userId'):
                harley_quin['username'] = username
                harley_quin['task'] = i.get('title')
                harley_quin['completed'] = i.get('completed')
                joker.append(harley_quin)
        wonder_woman[user_id] = joker

    with open("todo_all_employees.json", "w") as file:
        json.dump(wonder_woman, file)
