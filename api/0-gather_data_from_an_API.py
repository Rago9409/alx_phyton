import json
import requests

def export_all_employee_todo_to_json():
    # Endpoint URL
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    employee_url = "https://jsonplaceholder.typicode.com/users"

    # Fetching employee details
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    # Creating JSON object
    json_data = {}
    for employee in employee_data:
        employee_id = str(employee["id"])
        employee_name = employee["name"]
        json_data[employee_id] = []
        todos_response = requests.get(f"{todos_url}?userId={employee_id}")
        todos_data = todos_response.json()
        for task in todos_data:
            json_data[employee_id].append({
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name
            })

    # Creating JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, "w") as jsonfile:
        json.dump(json_data, jsonfile)

    print(f"JSON file '{json_filename}' has been created successfully.")
