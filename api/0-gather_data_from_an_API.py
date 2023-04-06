#!/usr/bin/python3
""" using this REST API,
    returns information about his/her todo list progress
"""

import requests
from sys import argv


if __name__ == "__main__":
    response_users = requests.get('https://jsonplaceholder.typicode.com/users')
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    employees = response_users.json()
    todos = response_todos.json()
    id = int(argv[1])
    name = ''
    task_completed = 0
    total_tasks = 0
    task_title = ''
    for i in employees:
        if id == i.get('id'):
            name = i.get('name')
    for i in todos:
        if id == i.get('userId'):
            if i.get('completed') == True:
                task_completed += 1
            if i.get('completed') == False or i.get('completed') == True:
                total_tasks += 1
    print(
        f'Employee {name} is done with tasks({task_completed}/{total_tasks}):')

    for i in todos:
        if id == i.get('userId'):
            if i.get('completed') == True:
                task_title = i.get('title')
                print(f'\t {task_title}')