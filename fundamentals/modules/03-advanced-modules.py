"""Question: Create your own custom module named `calculator.py` that contains functions for addition, subtraction, multiplication, and division. Then, import and use this module in a separate script to perform calculations. Demonstrate that the module only runs its own test code when executed directly, not when imported."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Create a separate `.py` file for your module (e.g., calculator.py).
# - Use `if __name__ == '__main__':` at the bottom of your module to protect your test code.
# - Import functions in your main script using `from module import function`.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Create a new file called `calculator.py` in the same folder.
# - In that file, define functions like `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, and `divide(a, b)`.
# - At the bottom of `calculator.py`, add a test section inside `if __name__ == '__main__':` that only runs when the file is executed directly.
# - In your main script, use `import calculator` or `from calculator import add, subtract, multiply, divide`.
# - Test all functions to see that the module's `if __name__` block does not run.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by looking at how to build our custom module. You will need 
# to create a new file named `calculator.py` in the same directory as this script. 
# Inside it, we define our mathematical functions and protect our test code. We have 
# provided the exact contents of this new file below as a comment block so you can build it.

# --- Contents of calculator.py ---
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     if b == 0:
#         return "Error: Cannot divide by zero"
#     return a / b
#
# if __name__ == '__main__':
#     print("Testing calculator module...")
#     print(f"10 + 5 = {add(10, 5)}")
#     print(f"10 * 5 = {multiply(10, 5)}")
# ---------------------------------

# What we accomplished in this step:
# - We learned how to structure a standalone module file.
# - We defined four basic arithmetic functions for our module.
# - We included the special `if __name__ == '__main__':` block to prevent tests from running on import.


# Step 2
# Explanation: Now we will write our main script. Assuming you have created the 
# `calculator.py` file in the same folder, we can import it just like a built-in module. 
# We will use dot notation to access the functions. To ensure this script doesn't crash 
# if you haven't made the file yet, we will safely wrap it in a try-except block.

try:
    import calculator
    
    result_add = calculator.add(10, 5)
    result_mult = calculator.multiply(10, 5)
    
    print(f"10 + 5 = {result_add}")
    print(f"10 * 5 = {result_mult}")
    
except ImportError:
    print("Notice: Please create 'calculator.py' in this folder to see the code run!")

# What we accomplished in this step:
# - We imported our entire custom module using the `import` keyword.
# - We called functions from the module using dot notation (e.g., `calculator.add()`).


# Step 3
# Explanation: Sometimes we don't want to type the module name every time. 
# We can switch to selective imports using the `from ... import ...` syntax. 
# Let's import `add` and `subtract` directly and call them without the module prefix.

try:
    from calculator import add, subtract
    
    # Now we can call them directly without typing 'calculator.' first!
    result_add = add(20, 8)
    result_sub = subtract(20, 8)
    
    print(f"20 + 8 = {result_add}")
    print(f"20 - 8 = {result_sub}")
    
except ImportError:
    print("Notice: Please create 'calculator.py' in this folder to see the code run!")

# What we accomplished in this step:
# - We used the `from module import function` syntax for cleaner, shorter code.
# - We called the imported functions directly without using dot notation.


# Step 4
# Explanation: One of the most important concepts in Python modules is the 
# `if __name__ == '__main__':` block. When we import `calculator` in this script, 
# Python reads and loads the code inside `calculator.py`. However, because we used 
# that special `if` statement, the test code inside `calculator.py` does NOT run. 
# We only see the output from our main script, meaning our module is well-designed.

try:
    import calculator
    
    # Notice that when you run this, you will not see "Testing calculator module..."
    # printed to your terminal. The module's internal test code remains hidden!
    print("Successfully imported calculator. No internal test output was printed.")
    
except ImportError:
    print("Notice: Please create 'calculator.py' in this folder to see the code run!")

# What we accomplished in this step:
# - We verified that the module's internal test code does not execute upon import.
# - We understood the value of `if __name__ == '__main__':` for protecting execution logic.


# Step 5
# Explanation: Let's consolidate our main script. We will demonstrate both import 
# styles, test all four arithmetic operations, and provide the expected output. 
# This represents a complete, professional script interacting with a custom module.

try:
    # Import the whole module to use multiply and divide
    import calculator
    
    # Import specific functions for addition and subtraction
    from calculator import add, subtract
    
    # Test our imports:
    print("--- Custom Calculator Tests ---")
    
    # Using selective import
    print(f"15 + 7 = {add(15, 7)}")
    print(f"15 - 7 = {subtract(15, 7)}")
    
    # Using whole module import
    print(f"15 * 7 = {calculator.multiply(15, 7)}")
    print(f"15 / 7 = {calculator.divide(15, 7)}")
    
    # Expected Output Example:
    # --- Custom Calculator Tests ---
    # 15 + 7 = 22
    # 15 - 7 = 8
    # 15 * 7 = 105
    # 15 / 7 = 2.142857142857143
    
except ImportError:
    print("Notice: Please create 'calculator.py' in this folder to see the code run!")

# What we accomplished in this step:
# - We consolidated our code to show multiple import techniques in one place.
# - We tested all operations to ensure the entire custom module works seamlessly.

# ===============================================================================
# CONGRATULATIONS! 🎉
# You have successfully created, protected, and imported your very own custom module!
# By building `calculator.py`, you learned how to organize code into separate files 
# for better reusability. You also mastered the `if __name__ == '__main__':` pattern 
# to protect test code, and practiced different import styles (`import module` vs. 
# `from module import function`). This is a huge step toward writing large, 
# professional Python applications.
# Remember: The best way to learn is by doing! 🚀
