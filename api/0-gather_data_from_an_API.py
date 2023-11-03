#!/usr/bin/python3
"""Module"""

import requests
import sys

"""module"""

if __name__ == '__main__':
    employee_ID = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_ID)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/" \
        .format(employee_ID)
    
    user_info = requests.request('GET', user_url).json()
    todos_info = requests.request('GET', todos_url).json()

    EMPLOYEE_NAME = user_info["name"]
    TASK_COMPLETED = list(filter(lambda obj: (obj["completed"] is True), todos_info))

    NUMBER_OF_DONE_TASKS = len(TASK_COMPLETED)
    TOTAL_NUMBER_OF_TASKS = len(todos_info)

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME,NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    [print("\t" + task["title"]) for task in TASK_COMPLETED]
    