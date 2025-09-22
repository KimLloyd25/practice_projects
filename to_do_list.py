# This code implements a simple command-line to-do list application.
# It allows users to add, remove, and view tasks stored in a JSON file.
# The tasks are stored in a file named 'to_do_list.json'.
# The application provides a menu for user interaction and handles basic file operations.
# The code is structured to be easy to understand and modify for additional features if needed.

import json
import os

# Define the path to the JSON file where tasks will be stored
file = "to_do_list.json"

# Check if the file exists, if not create an empty to-do list
def load_to_do_list():
    if os.path.exists(file):
        with open(file, 'r') as f:
            return json.load(f)
    return []

# Function to save the current to-do list to the JSON file
def save_to_do_list(to_do_list):
    with open(file, 'w') as f:
        json.dump(to_do_list, f, indent=4)

# Functions to manage the to-do list
def add_task(task):
    to_do_list = load_to_do_list()
    to_do_list.append(task)
    save_to_do_list(to_do_list)

# Function to remove a task from the to-do list
def remove_task(task):
    to_do_list = load_to_do_list()
    if task in to_do_list:
        to_do_list.remove(task)
        save_to_do_list(to_do_list)

# Function to view all tasks in the to-do list
def view_tasks():
    to_do_list = load_to_do_list()
    if not to_do_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(to_do_list, start=1):
            print(f"{idx}. {task}")

# Main function to run the command-line interface
def main():
    # Load existing tasks or create a new list
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        # Process user input
        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
            print(f"Task '{task}' removed.")
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
