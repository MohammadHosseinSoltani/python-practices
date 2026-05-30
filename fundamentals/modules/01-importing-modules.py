"""Question: Import the math module and use at least three different functions from it (such as sqrt, ceil, and pi). Print the results with clear labels."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
# 
# Tips for success:
# - Remember to use the `import` keyword at the very top of your code.
# - Take a moment to explore what a module offers by using the dot notation (e.g., `math.`).
# - Test each function right after importing it to see what it returns.
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use `import math` to bring in the entire math module.
# - Access functions with the dot notation, like `math.sqrt(16)`.
# - Check the module's constants, such as `math.pi`.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by importing the `math` module. Python has many built-in 
# functions, but some are stored inside "modules" (libraries of code) that we must 
# explicitly bring into our program. We will use `import math` and then print a 
# constant that the module provides: the value of Pi.
import math

pi_value = math.pi
print(f"The value of Pi is roughly: {pi_value}")

# What we accomplished in this step:
# - Used the `import` keyword to bring the `math` module into our program.
# - Accessed a constant (`pi`) inside the module using dot notation (`math.pi`).


# Step 2
# Explanation: Now that we have the module imported, let's use one of its functions. 
# We'll use `math.sqrt()` to compute the square root of a number. Notice that we still 
# need to use `math.` before the function name so Python knows where to find it.
import math

pi_value = math.pi
print(f"The value of Pi is roughly: {pi_value}")

square_root = math.sqrt(25)
print(f"The square root of 25 is: {square_root}")

# What we accomplished in this step:
# - Called a function (`sqrt()`) from the imported `math` module.
# - Passed an argument (25) into the function and printed the returned result.


# Step 3
# Explanation: Let's add another useful mathematical function. The `math.ceil()` function 
# takes a decimal number and always rounds it UP to the nearest whole integer. This is 
# different from standard rounding!
import math

pi_value = math.pi
print(f"The value of Pi is roughly: {pi_value}")

square_root = math.sqrt(25)
print(f"The square root of 25 is: {square_root}")

rounded_up = math.ceil(4.2)
print(f"4.2 rounded up to the nearest integer is: {rounded_up}")

# What we accomplished in this step:
# - Demonstrated the `math.ceil()` function.
# - Showed how modules offer specialized tools that standard Python operations might not.


# Step 4
# Explanation: To get a better feel for the module, let's demonstrate two more functions. 
# We will use `math.floor()` (which always rounds DOWN) and `math.pow()` (which raises a 
# number to a specific power, similar to the `**` operator).
import math

pi_value = math.pi
print(f"The value of Pi is roughly: {pi_value}")

square_root = math.sqrt(25)
print(f"The square root of 25 is: {square_root}")

rounded_up = math.ceil(4.2)
print(f"4.2 rounded up to the nearest integer is: {rounded_up}")

rounded_down = math.floor(4.8)
print(f"4.8 rounded down to the nearest integer is: {rounded_down}")

power_result = math.pow(2, 3)
print(f"2 raised to the power of 3 is: {power_result}")

# What we accomplished in this step:
# - Explored additional functions: `math.floor()` and `math.pow()`.
# - Built a solid understanding of how to repeatedly call tools from an imported module.


# Step 5
# Explanation: Sometimes writing `math.` over and over becomes tedious. Python allows us 
# to import specific functions directly into our current file using the `from ... import ...` 
# syntax. When we do this, we no longer need the `math.` prefix for those specific items!
import math

# Traditional import usage
rounded_down = math.floor(4.8)
print(f"Using math.floor: {rounded_down}")

# Selective import
from math import sqrt, pi

direct_sqrt = sqrt(100)
print(f"Using direct sqrt: {direct_sqrt}")
print(f"Using direct pi: {pi}")

# What we accomplished in this step:
# - Learned the `from module import function` syntax.
# - Used the imported functions directly without the module prefix.


# Step 6
# Explanation: For our final step, let's consolidate everything into a clean, 
# well-commented demonstration block. We will use the direct import method for 
# a few functions and the standard import for others, to show both styles side by side.

import math
from math import sqrt, pi

# Test our code:
print("--- Using math constants ---")
print(f"Value of Pi (direct import): {pi}")               # Expected output: 3.141592653589793
print(f"Value of e (standard import): {math.e}")          # Expected output: 2.718281828459045

print("\n--- Using math functions ---")
# Using the directly imported sqrt function
print(f"Square root of 81: {sqrt(81)}")                   # Expected output: 9.0

# Using functions accessed via the math module
print(f"Ceiling of 7.1 (round up): {math.ceil(7.1)}")     # Expected output: 8
print(f"Floor of 7.9 (round down): {math.floor(7.9)}")    # Expected output: 7
print(f"3 to the power of 4: {math.pow(3, 4)}")           # Expected output: 81.0

# What we accomplished in this step:
# - Created a comprehensive test block with descriptive labels.
# - Mixed both import styles successfully in the same script.
# - Documented the expected output using comments for easy verification.


# CONGRATULATIONS! 🎉
# You have successfully learned how to import and use external modules in Python!
# 
# Key takeaways:
# - The `import module_name` syntax gives you access to a massive library of tools.
# - You access a module's contents using "dot notation" (e.g., `math.sqrt()`).
# - You can use `from module_name import function_name` to import specific tools 
#   so you don't have to type the module's name every time.
# - Modules like `math` provide constants (like `pi`) as well as functions.
# 
# Keep experimenting! Try importing the `random` module and see if you can figure 
# out how to generate a random number using `random.randint(1, 10)`.
# 
# Remember: The best way to learn is by doing! 🚀
