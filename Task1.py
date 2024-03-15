import sqlite3

import datetime

# Connect to the SQLite database
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create a table for tasks
cursor.execute(
    """CREATE TABLE IF NOT EXISTS tasks (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       priority TEXT,
       due_date DATE,
       completed BOOLEAN DEFAULT 0
    )"""
)
conn.commit()

def add_task():
    name = input("Enter task name: ")
    priority = input("Enter task priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")  # Optional input
    
    if due_date:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()

    cursor.execute(
        "INSERT INTO tasks (name, priority, due_date) VALUES (?, ?, ?)",
        (name, priority, due_date)
    )
    conn.commit()

def remove_task():
    task_id = int(input("Enter task ID to remove: "))
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

def complete_task():
    task_id = int(input("Enter task ID to mark as completed: "))
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()

def display_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    for task in tasks:
        task_id, name, priority, due_date, completed = task
        print(f"ID: {task_id}, Name: {name}, Priority: {priority}, Due Date: {due_date}, Completed: {completed}")

# Main program loop
while True:
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. Display Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        display_tasks()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection when done
conn.close()
