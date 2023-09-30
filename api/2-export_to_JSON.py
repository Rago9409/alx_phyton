#fetching employee,TODO lists and counting completed tasks
import json
import requests

def export_employee_todo_to_json(employee_id):
    # Endpoint URLs
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # Fetching employee details
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    # Fetching TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Creating JSON object
    json_data = {str(employee_id): []}
    for task in todos_data:
        json_data[str(employee_id)].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        })

    # Creating JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, "w") as jsonfile:
        json.dump(json_data, jsonfile)

    print(f"JSON file '{json_filename}' has been created successfully.")

