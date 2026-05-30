"""Question: Write a function that calculates the area of a rectangle. The function should accept two parameters (length and width), with width being optional (defaulting to None). If only one argument is given, treat it as a square (area = side × side). Return the calculated area."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Set a default value for the `width` parameter in the function definition.
# - Use an `if` statement to check if `width` is `None`, and if so, set it equal to `length`.
# - Remember to use the `return` keyword to send the final calculated area back to the caller.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Define the function as `def calculate_area(length, width=None):`.
# - Inside the function, check if `width` is `None`. If so, set `width = length` (making it a square).
# - Calculate the area as `length * width` and `return` it.
# - Call the function with both one and two arguments to test both behaviors.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by defining a basic function named `calculate_area`. 
# For now, it will require both `length` and `width` as parameters. We will calculate 
# the area by multiplying them together, and then use the `return` keyword to pass 
# that value back to wherever the function was called.

def calculate_area(length, width):
    area = length * width
    return area

# Test the function with two arguments
rectangle_area = calculate_area(5, 4)
print(f"Area of 5x4 rectangle: {rectangle_area}")

# What we accomplished in this step:
# - We created a basic function that accepts two required parameters.
# - We calculated the area and returned it.
# - We tested the function by passing two arguments and printing the result.


# Step 2
# Explanation: Now we'll make the second parameter optional. We do this by assigning 
# it a default value of `None` right in the function definition. Inside the function, 
# we add a check: if `width` is still `None` (meaning the user didn't provide it), 
# we assume they want a square and set `width` equal to `length`.

def calculate_area(length, width=None):
    if width is None:
        width = length
        
    area = length * width
    return area

# Test with two arguments (rectangle)
rectangle_area = calculate_area(5, 4)
print(f"Area of 5x4 rectangle: {rectangle_area}")

# Test with one argument (square)
square_area = calculate_area(5)
print(f"Area of 5x5 square: {square_area}")

# What we accomplished in this step:
# - We introduced a default parameter value (`width=None`).
# - We added logic to handle the case when the optional argument is missing.
# - We successfully calculated the area for both a rectangle and a square using the same function.


# Step 3
# Explanation: In Python, we don't always have to rely on the order of arguments. 
# We can pass them by name, which are called "keyword arguments". Let's demonstrate 
# calling our function using keyword arguments to show that the order doesn't matter 
# when we explicitly name them.

def calculate_area(length, width=None):
    if width is None:
        width = length
        
    area = length * width
    return area

# Using standard positional arguments
area_positional = calculate_area(10, 2)

# Using keyword arguments (we can even reverse the order!)
area_keyword = calculate_area(width=2, length=10)

print(f"Area using positional arguments: {area_positional}")
print(f"Area using keyword arguments: {area_keyword}")

# What we accomplished in this step:
# - We learned how to call functions using keyword arguments.
# - We demonstrated that naming arguments provides clarity and flexibility in how we call functions.


# Step 4
# Explanation: It is a professional best practice to document what a function does. 
# We do this using a "docstring" (a multi-line string enclosed in triple quotes) 
# placed immediately after the function definition. This explains the purpose, 
# parameters, and return values to other developers.

def calculate_area(length, width=None):
    """
    Calculate the area of a rectangle or square.
    
    Parameters:
    length (int or float): The length of the shape.
    width (int or float, optional): The width of the shape. Defaults to None.
    
    Returns:
    int or float: The calculated area.
    """
    if width is None:
        width = length
        
    area = length * width
    return area

# What we accomplished in this step:
# - We added a professional docstring to our function.
# - We made our code self-documenting and much easier for others to understand.


# Step 5
# Explanation: Let's consolidate everything into a final, clean script. We will 
# structure our test block clearly to show all the different ways we can call 
# our newly built, robust function, and we'll add comments showing the expected output.

def calculate_area(length, width=None):
    """
    Calculate the area of a rectangle or square.
    
    Parameters:
    length (int or float): The length of the shape.
    width (int or float, optional): The width of the shape. Defaults to None.
    
    Returns:
    int or float: The calculated area.
    """
    if width is None:
        width = length
        
    return length * width

# Test our function:
print("--- Geometry Calculator ---")

# Scenario 1: Providing both arguments (Rectangle)
rect_area = calculate_area(8, 3)
print(f"Rectangle (8x3) Area: {rect_area}")
# Expected output: Rectangle (8x3) Area: 24

# Scenario 2: Providing only one argument (Square)
sq_area = calculate_area(6)
print(f"Square (6x6) Area: {sq_area}")
# Expected output: Square (6x6) Area: 36

# Scenario 3: Using keyword arguments
kw_area = calculate_area(width=5, length=7)
print(f"Rectangle (7x5) Area using keywords: {kw_area}")
# Expected output: Rectangle (7x5) Area using keywords: 35

# What we accomplished in this step:
# - We cleaned up the function by returning the calculation directly (`return length * width`).
# - We built a comprehensive demonstration block showing positional, default, and keyword argument behaviors.


# CONGRATULATIONS! 🎉
# You have successfully mastered intermediate function concepts in Python!
# You learned how to use optional parameters with default values (like `None`), 
# how to safely handle missing arguments inside your function body, and how 
# to call functions clearly using keyword arguments. You also practiced writing 
# professional docstrings to document your code. 
# Remember: The best way to learn is by doing! 🚀
