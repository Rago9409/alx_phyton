import requests

def get_employee_todo_progress(employee_id):
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

    # Counting completed tasks
    completed_tasks = [task for task in todos_data if task["completed"]]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    # Displaying progress
    print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

