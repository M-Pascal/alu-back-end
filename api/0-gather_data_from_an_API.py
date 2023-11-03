#!/usr/bin/python3
"""Module to fetch and display employee tasks"""

import requests
import sys

def fetch_employee_data(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_info = user_response.json()
        todos_info = todos_response.json()
        return user_info, todos_info
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def print_employee_tasks(employee_name, completed_tasks, total_tasks):
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"    {task['title']}")

if __name__ == '__main__':
    # Check the number of command line arguments
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    try:
        employee_ID = int(sys.argv[1])
    except ValueError:
        print("Error: Invalid employee ID. Please provide a valid integer.")
        sys.exit(1)

    user_info, todos_info = fetch_employee_data(employee_ID)
    employee_name = user_info.get("name", "Unknown Employee")
    completed_tasks = [task for task in todos_info if task["completed"]]
    total_tasks = len(todos_info)

    print_employee_tasks(employee_name, completed_tasks, total_tasks)
