#!/user/bin/python3
"""
    Using what you did in the task #0, extend your Python script
    to export data in the CSV format
"""

import requests
from sys import argv
import csv


if __name__ == "__main__":
    response_users = requests.get('https://jsonplaceholder.typicode.com/users')
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    employees = response_users.json()
    todos = response_todos.json()
    id = int(argv[1])
    username = ''
    completed = ''
    task_title = ''

    for i in employees:
        if id == i.get('id'):
            username = i.get('username')
    batman = open(str(argv[1]) + ".csv", "w")
    robin = csv.writer(batman, quoting=csv.QUOTE_ALL)
    for i in todos:
        paper = []
        if id == i.get('userId'):
            completed = i.get('completed')
            task_title = i.get('title')
            paper.append(str(id))
            paper.append(username)
            paper.append(completed)
            paper.append(task_title)
            robin.writerow(paper)
    batman.close()
