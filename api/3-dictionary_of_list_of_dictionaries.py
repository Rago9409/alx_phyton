"""fetching employee,TODO lists and counting completed tasks
"""
import json
import requests

def get_all_employee_todo_progress():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    employees = response.json()

    data = {}
    for employee in employees:
        employee_id = employee['id']
        url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        response = requests.get(url)
        todos = response.json()

        data[employee_id] = []
        for todo in todos:
            data[employee_id].append({
                "username": employee['username'],
                "task": todo['title'],
                "completed": todo['completed']
            })

    with open("todo_all_employees.json", mode='w') as file:
        json.dump(data, file)

if __name__ == '__main__':
    get_all_employee_todo_progress()
