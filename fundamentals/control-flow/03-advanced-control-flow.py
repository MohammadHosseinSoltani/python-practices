"""Question: Build a simple menu-driven program that runs continuously until the user chooses to quit. The menu should offer at least four options (e.g., check if a number is even/odd, calculate factorial iteratively, print a multiplication table, and exit). Use nested loops and conditionals to handle each operation and to validate user input."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Structure the code with functions for each menu option.
# - Use a `while True` loop for the main menu.
# - Handle invalid menu choices gracefully.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Define separate functions for each operation: `is_even_odd()`, `factorial()`, `multiplication_table()`, and a `main()` function for the menu loop.
# - Inside the menu loop, use `input()` to get the user's choice.
# - For factorial, use a `for` loop to accumulate the product. Be careful with negative inputs!
# - For the multiplication table, ask the user for a number and then use a `for` loop to print the table from 1 to 10.
# - Validate menu choices: if the user enters something other than 1-4, print an error and show the menu again.
# - Use `try/except` when converting numeric input to handle errors gracefully.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by creating the main menu loop. We will use a `while True:` 
# loop so the menu keeps appearing until the user explicitly decides to quit. We 
# will display the options, get the user's choice, and implement the "Exit" 
# option using the `break` statement.

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Check Even or Odd")
        print("2. Calculate Factorial")
        print("3. Print Multiplication Table")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '4':
            print("Exiting the program. Goodbye!")
            break
        elif choice in ['1', '2', '3']:
            print(f"You selected option {choice}. We will build this next!")
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# What we accomplished in this step:
# - We set up an infinite loop for our application's main menu.
# - We provided an exit mechanism to break out of the loop safely.
# - We added basic input validation for the menu choice.


# Step 2
# Explanation: Now we'll implement the logic for Option 1 (Even/Odd). We will 
# ask the user for a number, convert it to an integer inside a `try/except` 
# block to prevent crashes, and use the modulo operator (`%`) to check its parity.

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Check Even or Odd")
        print("2. Calculate Factorial")
        print("3. Print Multiplication Table")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            try:
                num = int(input("Enter an integer: "))
                if num % 2 == 0:
                    print(f"{num} is Even.")
                else:
                    print(f"{num} is Odd.")
            except ValueError:
                print("Invalid input! Please enter a valid whole number.")
                
        elif choice == '2':
            print("Factorial feature coming soon!")
            
        elif choice == '3':
            print("Multiplication table feature coming soon!")
            
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# What we accomplished in this step:
# - We added a working Even/Odd checker inside our menu loop.
# - We used `try/except` to ensure bad input doesn't crash the whole application.


# Step 3
# Explanation: Let's add Option 2: calculating a factorial. The factorial of a 
# number (n!) is the product of all positive integers less than or equal to n. 
# We will use a `for` loop to accumulate this product. We must also check that 
# the user doesn't enter a negative number, as factorials aren't defined for them.

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Check Even or Odd")
        print("2. Calculate Factorial")
        print("3. Print Multiplication Table")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            try:
                num = int(input("Enter an integer: "))
                if num % 2 == 0:
                    print(f"{num} is Even.")
                else:
                    print(f"{num} is Odd.")
            except ValueError:
                print("Invalid input! Please enter a valid whole number.")
                
        elif choice == '2':
            try:
                num = int(input("Enter a non-negative integer: "))
                if num < 0:
                    print("Error: Factorial is not defined for negative numbers.")
                else:
                    result = 1
                    # Loop from 1 to num (inclusive)
                    for i in range(1, num + 1):
                        result = result * i
                    print(f"The factorial of {num} is {result}.")
            except ValueError:
                print("Invalid input! Please enter a valid whole number.")
                
        elif choice == '3':
            print("Multiplication table feature coming soon!")
            
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# What we accomplished in this step:
# - We implemented an iterative factorial calculation using a `for` loop.
# - We added logical validation to prevent negative inputs.


# Step 4
# Explanation: Next, we add Option 3: printing a multiplication table. This 
# requires another `for` loop to iterate from 1 to 10, multiplying the user's 
# number by the loop counter.

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Check Even or Odd")
        print("2. Calculate Factorial")
        print("3. Print Multiplication Table")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            try:
                num = int(input("Enter an integer: "))
                if num % 2 == 0:
                    print(f"{num} is Even.")
                else:
                    print(f"{num} is Odd.")
            except ValueError:
                print("Invalid input! Please enter a valid whole number.")
                
        elif choice == '2':
            try:
                num = int(input("Enter a non-negative integer: "))
                if num < 0:
                    print("Error: Factorial is not defined for negative numbers.")
                else:
                    result = 1
                    for i in range(1, num + 1):
                        result = result * i
                    print(f"The factorial of {num} is {result}.")
            except ValueError:
                print("Invalid input! Please enter a valid whole number.")
                
        elif choice == '3':
            try:
                num = int(input("Enter an integer for the table: "))
                print(f"\nMultiplication Table for {num}:")
                for i in range(1, 11):
                    print(f"{num} x {i} = {num * i}")
            except ValueError:
                print("Invalid input! Please enter a valid whole number.")
                
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# What we accomplished in this step:
# - We completed the last functional requirement of our menu using a simple `for` loop.
# - We successfully nested loops: a `for` loop running inside our main `while` loop.


# Step 5
# Explanation: While our code works, stuffing everything into one massive `main()` 
# function makes it hard to read and maintain. Let's practice good software design 
# by breaking our code down into smaller, focused functions. We will consolidate 
# everything into a clean script and provide an example run block.

def is_even_odd():
    """Checks if a given number is even or odd."""
    try:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(f"> {num} is Even.")
        else:
            print(f"> {num} is Odd.")
    except ValueError:
        print("> Invalid input! Please enter a valid whole number.")


def calculate_factorial():
    """Calculates the factorial of a positive integer."""
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("> Error: Factorial is not defined for negative numbers.")
        else:
            result = 1
            for i in range(1, num + 1):
                result *= i
            print(f"> The factorial of {num} is {result}.")
    except ValueError:
        print("> Invalid input! Please enter a valid whole number.")


def multiplication_table():
    """Prints the multiplication table from 1 to 10 for a given number."""
    try:
        num = int(input("Enter an integer for the table: "))
        print(f"\n> Multiplication Table for {num}:")
        for i in range(1, 11):
            print(f"  {num} x {i} = {num * i}")
    except ValueError:
        print("> Invalid input! Please enter a valid whole number.")


def main():
    """Runs the main menu loop."""
    while True:
        print("\n" + "="*30)
        print("          MAIN MENU          ")
        print("="*30)
        print("1. Check Even or Odd")
        print("2. Calculate Factorial")
        print("3. Print Multiplication Table")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")
        
        if choice == '1':
            is_even_odd()
        elif choice == '2':
            calculate_factorial()
        elif choice == '3':
            multiplication_table()
        elif choice == '4':
            print("> Exiting the program. Goodbye!")
            break
        else:
            print("> Invalid choice! Please enter a number between 1 and 4.")

# Test our code:
# Uncomment the line below to run the interactive program
# main()

# Example run:
# ==============================
#           MAIN MENU          
# ==============================
# 1. Check Even or Odd
# 2. Calculate Factorial
# 3. Print Multiplication Table
# 4. Exit
# 
# Select an option (1-4): 2
# Enter a non-negative integer: 5
# > The factorial of 5 is 120.
# 
# ==============================
#           MAIN MENU          
# ==============================
# 1. Check Even or Odd
# 2. Calculate Factorial
# 3. Print Multiplication Table
# 4. Exit
# 
# Select an option (1-4): 4
# > Exiting the program. Goodbye!

# What we accomplished in this step:
# - We refactored our code into modular functions, separating concerns.
# - We drastically improved the readability of the `main()` function.
# - We demonstrated a clean execution flow in the comments.


# CONGRATULATIONS! 🎉
# You have successfully built an advanced, menu-driven Python application!
# You practiced managing control flow using a continuous `while` loop, nesting
# conditionals and `for` loops within it, and handling bad input gracefully.
# By refactoring the final step, you also took a massive leap forward in software 
# design, learning how function decomposition makes complex programs manageable.
# Remember: The best way to learn is by doing! 🚀
