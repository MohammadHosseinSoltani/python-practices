"""Project: Build a command-line to-do list manager. The program should allow the user to add tasks, view all tasks, mark tasks as completed, and delete tasks. Tasks should persist in memory during the session (no file saving required)."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Think about storing your tasks as a list of dictionaries to easily manage task descriptions and their completion status.
# - You will need a main loop that displays a menu of options to the user and waits for their choice.
# - Make sure you handle invalid menu choices and invalid task numbers gracefully!
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Store tasks as a list of dictionaries, where each dictionary has keys like 'task' (string) and 'completed' (boolean).
# - Use a `while True:` loop to show a menu with options: 1. Add Task, 2. View Tasks, 3. Complete Task, 4. Delete Task, 5. Quit.
# - For viewing tasks, loop through the list and print each task with its index and status (e.g., `[X]` for completed, `[ ]` for pending).
# - For completing a task, ask for the task number, check if it's valid, and set its 'completed' to True.
# - For deleting a task, ask for the task number, validate it, and remove it from the list using `pop()`.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by setting up the core structure of our application. We 
# need an empty list to store our tasks, and a continuous loop that presents a menu 
# to the user. We will ask for their choice and simply print it out for now to make 
# sure our input collection is working. We will also add a temporary break so the 
# loop doesn't run infinitely while we test.

tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Quit")
    
    choice = input("Enter your choice (1-5): ")
    print(f"You chose option: {choice}")
    
    break  # Temporary break for testing

# What we accomplished in this step:
# - Created an empty `tasks` list to hold our data.
# - Set up a `while True:` loop to keep the application running.
# - Built and displayed a simple user menu.
# - Collected user input.


# Step 2
# Explanation: Now we'll implement the "Add Task" feature. When the user chooses option '1', 
# we ask them what the task is. Then, we create a dictionary representing that task. 
# The dictionary will hold the task description and a boolean indicating it is not 
# completed yet. We append this to our `tasks` list. We also remove the temporary 
# break so the menu reappears after adding a task.

tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Quit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        task_desc = input("Enter the task description: ")
        # Create a new task dictionary and add it to our list
        new_task = {"task": task_desc, "completed": False}
        tasks.append(new_task)
        print(f"Task '{task_desc}' added successfully!")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        # A temporary placeholder for other options
        print("Option not implemented yet.")

# What we accomplished in this step:
# - Used an `if/elif` structure to handle menu choices.
# - Stored complex data (a string and a boolean) together using a dictionary.
# - Successfully added new tasks to our list.
# - Added the "Quit" functionality so we can exit safely.


# Step 3
# Explanation: Next, let's implement option '2': View Tasks. We need to iterate over 
# our `tasks` list and display them. We will use `enumerate(tasks, 1)` to automatically 
# number them starting at 1. We will also check the `completed` status to show a `[X]` 
# for done and a `[ ]` for pending. If the list is empty, we should let the user know.

tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Quit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        task_desc = input("Enter the task description: ")
        new_task = {"task": task_desc, "completed": False}
        tasks.append(new_task)
        print(f"Task '{task_desc}' added successfully!")
        
    elif choice == '2':
        print("\n--- Your Tasks ---")
        if not tasks:
            print("Your to-do list is empty.")
        else:
            for index, item in enumerate(tasks, 1):
                # Determine what symbol to show based on completion status
                status = "[X]" if item["completed"] else "[ ]"
                print(f"{index}. {status} {item['task']}")
                
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Option not implemented yet.")

# What we accomplished in this step:
# - Handled empty states gracefully.
# - Used `enumerate()` to display user-friendly, 1-based indexing.
# - Used a concise inline `if` statement to format the completion status nicely.


# Step 4
# Explanation: Now we implement option '3': Complete Task. We ask the user for the 
# number of the task they want to complete. Because lists are zero-indexed, we must 
# subtract 1 from their input to find the correct dictionary in our list. We also 
# need to wrap our input conversion in a `try/except` block to handle cases where 
# they type letters instead of numbers, or provide a number that doesn't exist.

tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Quit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        task_desc = input("Enter the task description: ")
        new_task = {"task": task_desc, "completed": False}
        tasks.append(new_task)
        print(f"Task '{task_desc}' added successfully!")
        
    elif choice == '2':
        print("\n--- Your Tasks ---")
        if not tasks:
            print("Your to-do list is empty.")
        else:
            for index, item in enumerate(tasks, 1):
                status = "[X]" if item["completed"] else "[ ]"
                print(f"{index}. {status} {item['task']}")
                
    elif choice == '3':
        if not tasks:
            print("No tasks to complete!")
            continue
            
        try:
            task_num = int(input("Enter task number to mark as complete: "))
            # Check if the number is within the valid range of our list
            if 1 <= task_num <= len(tasks):
                # Access the dictionary and update the boolean value
                tasks[task_num - 1]["completed"] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
            
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Option not implemented yet.")

# What we accomplished in this step:
# - Safely converted string inputs to integers using `try/except`.
# - Translated user-friendly numbering (1-based) to Python's internal numbering (0-based).
# - Updated values inside a dictionary stored within a list.


# Step 5
# Explanation: Let's implement option '4': Delete Task. The logic is almost identical 
# to completing a task. We ask for a number, validate it, convert it to an index, 
# and then use Python's built-in `pop()` method to remove the item entirely from the 
# list. We will capture the returned popped item so we can print a friendly confirmation.

tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Quit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        task_desc = input("Enter the task description: ")
        new_task = {"task": task_desc, "completed": False}
        tasks.append(new_task)
        print(f"Task '{task_desc}' added successfully!")
        
    elif choice == '2':
        print("\n--- Your Tasks ---")
        if not tasks:
            print("Your to-do list is empty.")
        else:
            for index, item in enumerate(tasks, 1):
                status = "[X]" if item["completed"] else "[ ]"
                print(f"{index}. {status} {item['task']}")
                
    elif choice == '3':
        if not tasks:
            print("No tasks to complete!")
            continue
            
        try:
            task_num = int(input("Enter task number to mark as complete: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
            
    elif choice == '4':
        if not tasks:
            print("No tasks to delete!")
            continue
            
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                # pop() removes and returns the item at the given index
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['task']}' deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
            
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

# What we accomplished in this step:
# - Implemented full CRUD (Create, Read, Update, Delete) functionality for our tasks.
# - Handled edge cases where the user tries to delete from an empty list.
# - Used the `pop()` method effectively.


# Step 6
# Explanation: For our final step, let's wrap everything inside a function called 
# `run_todo_app()`. This keeps our global scope clean and makes the script reusable. 
# We'll also provide a comprehensive example run in the comments below so you can see 
# the expected interaction.

def run_todo_app():
    tasks = []
    
    print("Welcome to your Python To-Do List Manager!")
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            task_desc = input("Enter the task description: ")
            new_task = {"task": task_desc, "completed": False}
            tasks.append(new_task)
            print(f"Task '{task_desc}' added successfully!")
            
        elif choice == '2':
            print("\n--- Your Tasks ---")
            if not tasks:
                print("Your to-do list is empty.")
            else:
                for index, item in enumerate(tasks, 1):
                    status = "[X]" if item["completed"] else "[ ]"
                    print(f"{index}. {status} {item['task']}")
                    
        elif choice == '3':
            if not tasks:
                print("No tasks to complete!")
                continue
                
            try:
                task_num = int(input("Enter task number to mark as complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    print("Task marked as complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '4':
            if not tasks:
                print("No tasks to delete!")
                continue
                
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task['task']}' deleted!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '5':
            print("Goodbye! Exiting To-Do App.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    run_todo_app()

# Example run:
#
# Welcome to your Python To-Do List Manager!
# 
# --- To-Do List Menu ---
# 1. Add Task
# 2. View Tasks
# 3. Complete Task
# 4. Delete Task
# 5. Quit
# Enter your choice (1-5): 1
# Enter the task description: Buy groceries
# Task 'Buy groceries' added successfully!
#
# --- To-Do List Menu ---
# ...
# Enter your choice (1-5): 2
# 
# --- Your Tasks ---
# 1. [ ] Buy groceries
#
# --- To-Do List Menu ---
# ...
# Enter your choice (1-5): 3
# Enter task number to mark as complete: 1
# Task marked as complete!
#
# --- To-Do List Menu ---
# ...
# Enter your choice (1-5): 2
# 
# --- Your Tasks ---
# 1. [X] Buy groceries
#
# --- To-Do List Menu ---
# ...
# Enter your choice (1-5): 5
# Goodbye! Exiting To-Do App.


# CONGRATULATIONS! 🎉
# You've built a robust, menu-driven command-line application!
#
# Key takeaways:
# - Data Management: You combined lists and dictionaries to organize complex data gracefully.
# - Menu-Driven Apps: You learned how to keep an application running continuously, offering a suite of tools to the user.
# - Input Validation: You protected your app against unexpected user behavior (like typing words instead of numbers, or choosing non-existent options).
# - User-Friendly Output: You translated internal data states (like `True` or `False`) into visual cues (`[X]` or `[ ]`) that users easily understand.
#
# Remember: The best way to learn is by doing! 🚀
