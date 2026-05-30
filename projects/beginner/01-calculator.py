"""Project: Build a simple command-line calculator that can perform addition, subtraction, multiplication, and division. The program should repeatedly ask the user for two numbers and an operator until the user types 'quit'."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Plan the program flow before you start typing. You will need to take inputs, process them, and output a result.
# - Think about handling invalid inputs (like someone typing "hello" instead of a number).
# - Use a while loop for continuous operation so the user doesn't have to restart the script for every calculation.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use a `while True:` loop to keep the calculator running.
# - Ask the user for input with `input()`, and convert numbers with `float()`.
# - Use `if`/`elif`/`else` to choose the correct operation based on the operator symbol.
# - Handle division by zero and invalid operators with friendly messages.
# - Allow the user to type 'quit' to exit the loop.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by setting up the core loop of our application. We want 
# the calculator to run continuously, so we use a `while True:` loop. Inside the loop, 
# we ask the user for two numbers using the `input()` function. We will print them 
# back just to verify our input collection works. (We add a temporary `break` at the 
# end so this step doesn't loop infinitely while you test it!)

while True:
    print("--- New Calculation ---")
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")
    
    print(f"You entered: {num1_str} and {num2_str}")
    
    # Temporary break to prevent an infinite loop during early testing
    break

# What we accomplished in this step:
# - Set up a continuous `while` loop structure.
# - Collected user input as strings using `input()`.
# - Printed the raw input back to the user.


# Step 2
# Explanation: Now we'll add the mathematical logic. We need to ask the user for an 
# operator (+, -, *, /). Since `input()` always returns a string, we must convert 
# our number strings into actual numbers using `float()`. Then, we use an 
# `if`/`elif`/`else` block to determine which mathematical operation to perform based 
# on the chosen operator, and print the result.

while True:
    print("--- New Calculation ---")
    num1_str = input("Enter the first number: ")
    operator = input("Enter an operator (+, -, *, /): ")
    num2_str = input("Enter the second number: ")
    
    # Convert the string inputs into floating-point numbers
    num1 = float(num1_str)
    num2 = float(num2_str)
    
    # Perform the chosen operation
    if operator == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operator == "/":
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Unknown operator. Please use +, -, *, or /.")
        
    break  # Temporary break for testing

# What we accomplished in this step:
# - Asked the user for an operator.
# - Converted the string inputs to floats so we can perform math on them.
# - Built the control flow to perform addition, subtraction, multiplication, or division.


# Step 3
# Explanation: What happens if the user types "apple" instead of a number? The 
# `float()` function will crash our program! We need to add input validation. 
# We'll wrap our conversion in a `try`/`except` block. If a `ValueError` occurs, 
# we'll print a friendly error message and use the `continue` keyword to jump back 
# to the top of the loop and start over, preventing the crash.

while True:
    print("--- New Calculation ---")
    num1_str = input("Enter the first number: ")
    operator = input("Enter an operator (+, -, *, /): ")
    num2_str = input("Enter the second number: ")
    
    # Try to convert the inputs, handle errors gracefully if they aren't numbers
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("Error: Please enter valid numeric values!")
        continue  # Skip the rest of the loop and start over
        
    if operator == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operator == "/":
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Unknown operator. Please use +, -, *, or /.")
        
    break  # Temporary break for testing

# What we accomplished in this step:
# - Introduced a `try`/`except` block to catch `ValueError`.
# - Handled non-numeric input gracefully without crashing the program.
# - Used `continue` to reset the loop upon an error.


# Step 4
# Explanation: There is another way our program can crash: dividing by zero. In math, 
# division by zero is undefined, and in Python, it raises a `ZeroDivisionError`. We 
# can prevent this by explicitly checking if `num2` is `0` inside our division block 
# before attempting the calculation.

while True:
    print("--- New Calculation ---")
    num1_str = input("Enter the first number: ")
    operator = input("Enter an operator (+, -, *, /): ")
    num2_str = input("Enter the second number: ")
    
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("Error: Please enter valid numeric values!")
        continue
        
    if operator == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operator == "/":
        # Check for division by zero before calculating
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Unknown operator. Please use +, -, *, or /.")
        
    break  # Temporary break for testing

# What we accomplished in this step:
# - Added a safety check to prevent `ZeroDivisionError`.
# - Improved the robustness of our calculator.


# Step 5
# Explanation: Our calculator is robust, but the user is trapped! We need to allow 
# them to type 'quit' to exit the loop. We will check the user's first input. If they 
# type 'quit' (converted to lowercase so 'QUIT' also works), we will `break` out of 
# the loop entirely. This means we can finally remove our temporary testing `break`!

while True:
    print("\n--- New Calculation ---")
    num1_str = input("Enter the first number (or 'quit' to exit): ")
    
    # Check if the user wants to exit
    if num1_str.lower() == 'quit':
        print("Goodbye!")
        break
        
    operator = input("Enter an operator (+, -, *, /): ")
    num2_str = input("Enter the second number: ")
    
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("Error: Please enter valid numeric values!")
        continue
        
    if operator == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Unknown operator. Please use +, -, *, or /.")

# What we accomplished in this step:
# - Implemented an exit strategy using the `break` keyword.
# - Used string methods (`lower()`) to make the quit command case-insensitive.
# - Removed the temporary break, creating a fully functioning, continuous application.


# Step 6
# Explanation: For the final step, we will consolidate our code into a clean, reusable 
# function called `run_calculator()`. This is a professional best practice. We will also 
# add a welcome message to make the program friendlier. Below the function, we include 
# an example run in the comments so you can see exactly how the terminal interaction looks.

def run_calculator():
    print("Welcome to the Python Command-Line Calculator!")
    print("You can perform basic math operations. Type 'quit' at any time to exit.")
    
    while True:
        print("\n--- New Calculation ---")
        num1_str = input("Enter the first number (or 'quit' to exit): ")
        
        if num1_str.lower() == 'quit':
            print("Thanks for using the calculator. Goodbye!")
            break
            
        operator = input("Enter an operator (+, -, *, /): ")
        num2_str = input("Enter the second number: ")
        
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("Error: Please enter valid numeric values!")
            continue
            
        if operator == "+":
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operator == "-":
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operator == "*":
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Unknown operator. Please use +, -, *, or /.")


if __name__ == "__main__":
    run_calculator()

# Example run:
# 
# Welcome to the Python Command-Line Calculator!
# You can perform basic math operations. Type 'quit' at any time to exit.
#
# --- New Calculation ---
# Enter the first number (or 'quit' to exit): 10
# Enter an operator (+, -, *, /): *
# Enter the second number: 5
# Result: 10.0 * 5.0 = 50.0
#
# --- New Calculation ---
# Enter the first number (or 'quit' to exit): apple
# Enter an operator (+, -, *, /): +
# Enter the second number: 2
# Error: Please enter valid numeric values!
#
# --- New Calculation ---
# Enter the first number (or 'quit' to exit): 10
# Enter an operator (+, -, *, /): /
# Enter the second number: 0
# Error: Cannot divide by zero!
#
# --- New Calculation ---
# Enter the first number (or 'quit' to exit): quit
# Thanks for using the calculator. Goodbye!


# CONGRATULATIONS! 🎉
# You've successfully built a complete, interactive Python application!
#
# Key takeaways:
# - Project Structure: You learned how to organize variables, loops, and conditions to create a continuous application.
# - User Input: You mastered collecting data from the terminal and converting string inputs into usable data types.
# - Control Flow: You utilized `if`, `elif`, `else`, `continue`, and `break` to precisely control how the program navigates different scenarios.
# - Error Handling: You anticipated user mistakes and prevented program crashes by using `try`/`except` and logical safety checks.
#
# Try extending this project! Can you add support for exponents (**), or allow the user to calculate the remainder (%)? 
# Remember: The best way to learn is by doing! 🚀
