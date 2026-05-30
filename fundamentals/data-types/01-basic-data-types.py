"""Question: Experiment with Python's basic data types (int, float, str, bool). Perform type conversions, check types, and demonstrate simple operations."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully to understand what is being asked.
# - Test small pieces of code one at a time.
# - Use the `type()` function to check your data types.
# - Experiment with conversion functions like `int()`, `float()`, and `str()`.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Think about what functions can change one type to another (like `int()`, `float()`, `str()`).
# - Remember that Boolean values are `True` and `False` (capitalized in Python).
# - Use `type()` to check the type of a value.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by defining two of the most common numerical data types: 
# an integer (whole number) and a float (decimal number). We will print their values 
# and use the `type()` function to see how Python categorizes them.
item_count = 5
item_price = 12.99

print("Count:", item_count, "| Type:", type(item_count))
print("Price:", item_price, "| Type:", type(item_price))

# What we accomplished in this step:
# - Created an integer variable (`int`).
# - Created a float variable (`float`).
# - Printed both the values and their corresponding types.


# Step 2
# Explanation: Now we'll add a string (text) and a Boolean (True/False value) to our program.
# Strings are enclosed in quotes, and Booleans must start with a capital letter in Python.
item_count = 5
item_price = 12.99

print("Count:", item_count, "| Type:", type(item_count))
print("Price:", item_price, "| Type:", type(item_price))

item_name = "Coffee Mug"
is_in_stock = True

print("Name:", item_name, "| Type:", type(item_name))
print("In Stock:", is_in_stock, "| Type:", type(is_in_stock))

# What we accomplished in this step:
# - Created a string variable (`str`).
# - Created a boolean variable (`bool`).
# - Verified their types using the `type()` function.


# Step 3
# Explanation: Often, we need to convert data from one type to another. This is called 
# "type casting" or "type conversion". We will convert our integer into a float using `float()`, 
# and our float into an integer using `int()`. Notice how converting a float to an int simply 
# drops the decimal portion!
item_count = 5
item_price = 12.99
item_name = "Coffee Mug"
is_in_stock = True

print("Count:", item_count, "| Type:", type(item_count))
print("Price:", item_price, "| Type:", type(item_price))
print("Name:", item_name, "| Type:", type(item_name))
print("In Stock:", is_in_stock, "| Type:", type(is_in_stock))

# Type conversions
count_as_float = float(item_count)
price_as_int = int(item_price)

print("Count as float:", count_as_float, "| Type:", type(count_as_float))
print("Price as int:", price_as_int, "| Type:", type(price_as_int))

# What we accomplished in this step:
# - Converted an `int` to a `float`.
# - Converted a `float` to an `int` (truncating the decimal part).
# - Printed the newly converted variables and their types.


# Step 4
# Explanation: A very common error in Python is trying to add a number directly to a string.
# To combine text and numbers using the `+` operator, we first need to convert the number 
# into a string using the `str()` function.
item_count = 5
item_price = 12.99
item_name = "Coffee Mug"
is_in_stock = True

count_as_float = float(item_count)
price_as_int = int(item_price)

# Converting a number to a string for concatenation
count_as_string = str(item_count)
inventory_message = "We have " + count_as_string + " units of " + item_name + " left."
print(inventory_message)

# What we accomplished in this step:
# - Converted a numeric type (`int`) to a string type (`str`).
# - Safely concatenated strings and variables using the `+` operator.


# Step 5
# Explanation: Booleans are perfect for making decisions in our code. We will use an 
# `if` statement to check if the item is in stock. If `is_in_stock` is True, we print 
# one message; if it is False, we print another.
item_count = 5
item_price = 12.99
item_name = "Coffee Mug"
is_in_stock = True

count_as_float = float(item_count)
price_as_int = int(item_price)

count_as_string = str(item_count)
inventory_message = "We have " + count_as_string + " units of " + item_name + " left."
print(inventory_message)

# Using a boolean in conditional logic
if is_in_stock:
    print("Good news: The item is available for purchase!")
else:
    print("Sorry, this item is currently out of stock.")

# What we accomplished in this step:
# - Used a Boolean variable to control the flow of the program.
# - Executed different code based on whether the Boolean was True or False.


# Step 6
# Explanation: For our final step, let's clean up our code and consolidate it into a clear, 
# readable demonstration block. We will organize our variables, perform our conversions, 
# and print everything neatly with expected outputs as comments.
# This makes it very easy to read and understand everything we've built.

# Test our code:
# 1. Define our basic data types
item_count = 5          # int
item_price = 12.99      # float
item_name = "Coffee Mug" # str
is_in_stock = True      # bool

print("--- Basic Types ---")
print("Count:", item_count, "->", type(item_count))          # Expected output: Count: 5 -> <class 'int'>
print("Price:", item_price, "->", type(item_price))          # Expected output: Price: 12.99 -> <class 'float'>
print("Name:", item_name, "->", type(item_name))             # Expected output: Name: Coffee Mug -> <class 'str'>
print("In Stock:", is_in_stock, "->", type(is_in_stock))     # Expected output: In Stock: True -> <class 'bool'>

# 2. Perform conversions
count_as_float = float(item_count)
price_as_int = int(item_price)
count_as_str = str(item_count)

print("\n--- Type Conversions ---")
print("Float count:", count_as_float, "->", type(count_as_float)) # Expected output: Float count: 5.0 -> <class 'float'>
print("Int price:", price_as_int, "->", type(price_as_int))       # Expected output: Int price: 12 -> <class 'int'>

# 3. Demonstrate operations
print("\n--- Operations ---")
message = "Inventory: " + count_as_str + " " + item_name + "s"
print(message)                                              # Expected output: Inventory: 5 Coffee Mugs

if is_in_stock:
    print("Status: Ready to ship!")                         # Expected output: Status: Ready to ship!
else:
    print("Status: Check back later.")

# What we accomplished in this step:
# - Grouped all our code into a final, professional script.
# - Formatted our output cleanly with descriptive labels.
# - Included expected output comments to verify our logic.


# CONGRATULATIONS! 🎉
# You have successfully mastered Python's basic data types!
# 
# Key takeaways:
# - Python has four foundational data types: int (whole numbers), float (decimals), 
#   str (text), and bool (True/False).
# - You can easily check the type of any variable using the `type()` function.
# - Converting data from one type to another (type casting) is simple using 
#   built-in functions like `int()`, `float()`, and `str()`.
# - Booleans are extremely powerful for controlling logic with `if/else` statements.
# 
# Try experimenting further: change the `is_in_stock` variable to `False` and run 
# the code again to see how the output changes, or try casting a string like "100" 
# into an integer!
# 
# Remember: The best way to learn is by doing! 🚀
