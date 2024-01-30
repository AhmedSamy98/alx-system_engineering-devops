#!/usr/bin/python3
"""This module request data from
jsonplaceholder"""
import requests
import sys


if __name__ == '__main__':
    end_point = "https://jsonplaceholder.typicode.com/"
    id = sys.argv[1]
    response = requests.get('{}users/{}'
                            .format(end_point, id)).json()
    name = response["name"]
    print('Employee {} is done with tasks'.format(name), end="")

    todos = requests.get('{}todos?userId={}'.
                         format(end_point, id)).json()
    complete = []
    for todo in todos:
        if todo['completed'] is True:
            complete.append(todo)
    print('({}/{}):'.format(len(complete), len(todos)))
    for task in complete:
        print('\t {}'.format(task['title']))
