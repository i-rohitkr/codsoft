# Define an empty list to store tasks
todo_list = []

# Function to add a task to the list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to display the current to-do list
def display_list():
    print("\nTo-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
    print()

# Function to remove a task from the list
def remove_task(task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index. Please enter a valid index.")

# Main program loop
while True:
    print("1. Add Task\n2. Display List\n3. Remove Task\n4. Quit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        display_list()
    elif choice == '3':
        task_index = int(input("Enter the index of the task to remove: "))
        remove_task(task_index)
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
