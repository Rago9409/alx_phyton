#fetching employee,TODO lists and counting completed tasks
import csv
import requests

def export_employee_todo_to_csv(employee_id):
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

    # Creating CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            writer.writerow([employee_id, employee_name, task["completed"], task["title"]])

    print(f"CSV file '{csv_filename}' has been created successfully.")


