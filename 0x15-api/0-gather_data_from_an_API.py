#!/usr/bin/python3
"""
script using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def fetch_employee_todo_list(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user info
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()

    # Fetch user's TODO list
    todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todo_data = todo_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]

    # Display information
    print(f"Employee {user_data['name']} is done with tasks "
          f"({len(completed_tasks)}/{len(todo_data)}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_list(employee_id)
