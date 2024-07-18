import main
import db_helper

def to_do_list():
    user_input = input("""--------------------------------
    1. Add Task
    2. Remove Task
    3. View Tasks
    4. Back to Main Menu
    Enter choice (Number):""")
    
    if user_input == "1":
        add_task()
    elif user_input == "2":
        remove_task()
    elif user_input == "3":
        view_tasks()
    elif user_input == "4":
        main.main()
    else:
        print("Invalid choice. Please try again.")
    
def add_task():
    try:
        description = input("Enter task description: ")
        date = input("Date (YYYY-MM-DD): ")
        time = input("Time (HH:MM): ")

        query = "INSERT INTO tasks (description, date, time) VALUES (?, ?, ?)"
        db_helper.execute_query(query, (description, date, time))

        print(f"Task '{description}' added successfully.")

        to_do_list()
    except Exception as e:
        print(f"Error: {e}")

def remove_task():
    try:
        task_id = input("Enter Task ID to remove: ")
        query = "DELETE FROM tasks WHERE id = ?"
        db_helper.execute_query(query, (task_id,))
        print("Task removed successfully.")

        to_do_list()
    except Exception as e:
        print(f"Error: {e}")

def view_tasks():
    try:
        query = "SELECT * FROM tasks"
        tasks = db_helper.fetch_query(query)
        print("To-Do List:")
        for task in tasks:
            print(task)
        
        print("--------------------------------")
        to_do_list()
    except Exception as e:
        print(f"Error: {e}")
