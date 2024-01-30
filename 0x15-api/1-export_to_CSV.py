#!/usr/bin/python3
"""
    Exports data in the CSV format
"""


from requests import get
from sys import argv
import csv


if __name__ == "__main__":

    userId = argv[1]
    user = get("https://jsonplaceholder.typicode.com/users/{}".format(userId))

    name = user.json().get('username')

    todos = get('https://jsonplaceholder.typicode.com/todos')

    filename = userId + '.csv'

    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == int(userId):
                writer.writerow([userId, name, str(task.get('completed')),
                                 task.get('title')])
