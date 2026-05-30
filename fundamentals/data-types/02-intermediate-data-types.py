"""Question: Write a program that takes a list containing mixed data types (integers, floats, strings, booleans). Loop through the list, print each item along with its data type, and calculate the sum of all numeric values (integers and floats), ignoring non-numeric items."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Use a for loop to iterate through the list.
# - Use the isinstance() function to check if an item is numeric.
# - Keep a running total to accumulate the sum.
# - Handle non-numeric items gracefully by simply skipping them.
# - Watch out for booleans—they can behave like integers in Python!
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use a `for` loop to iterate through the list.
# - Use `type()` or `isinstance()` to check the type of each item.
# - Keep a `total` variable that you only add to if the item is an `int` or `float`.
# - Remember that `bool` is a subclass of `int` in Python, so use `isinstance(item, bool)` to exclude booleans if you don't want them counted as numbers.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by creating a list of mixed data types. We will set 
# up a simple `for` loop to go through each item in the list and print its value. 
# This helps us ensure we are properly accessing every element.

mixed_data = [10, "Python", 5.5, False, True, 100, "Code", -2.5]

print("--- Step 1: Printing items ---")
for item in mixed_data:
    print(item)

# What we accomplished in this step:
# - We created a list containing integers, floats, strings, and booleans.
# - We successfully set up a loop to iterate through and print each item.


# Step 2
# Explanation: Now we'll add logic to print the data type of each item alongside 
# its value. We can use Python's built-in `type()` function to reveal what 
# kind of data we are working with on each iteration of the loop.

mixed_data = [10, "Python", 5.5, False, True, 100, "Code", -2.5]

print("\n--- Step 2: Printing items and their types ---")
for item in mixed_data:
    # We use an f-string to format the output nicely
    print(f"Item: {item} | Type: {type(item)}")

# What we accomplished in this step:
# - We utilized the `type()` function to inspect data types dynamically.
# - We improved our output formatting using f-strings.


# Step 3
# Explanation: Our main goal is to calculate the sum of numeric values. Let's 
# introduce a `total` variable. We will use `isinstance()` to check if an item 
# is an `int` or a `float` before adding it to our total. 

mixed_data = [10, "Python", 5.5, False, True, 100, "Code", -2.5]
total = 0

print("\n--- Step 3: Calculating numeric sum ---")
for item in mixed_data:
    print(f"Evaluating: {item}")
    
    # Check if the item belongs to either the int or float class
    if isinstance(item, (int, float)):
        total = total + item
        print(f"  -> Added. New total: {total}")

print(f"Final total after Step 3: {total}")

# What we accomplished in this step:
# - We introduced a running total variable to accumulate our sum.
# - We used `isinstance()` with a tuple of types `(int, float)` to filter our data.
# - Note: The total is 114.0 instead of 113.0 because True evaluates as 1 and False as 0!


# Step 4
# Explanation: In Step 3, we fell into a classic Python pitfall: `bool` is actually 
# a subclass of `int`! Because of this, `isinstance(True, int)` returns True, and 
# it gets added to our sum as the number 1. To fix this, we need to add an explicit 
# check to exclude booleans from our numeric calculation.

mixed_data = [10, "Python", 5.5, False, True, 100, "Code", -2.5]
total = 0

print("\n--- Step 4: Handling the boolean pitfall ---")
for item in mixed_data:
    # We ensure the item is a number AND explicitly NOT a boolean
    if isinstance(item, (int, float)) and not isinstance(item, bool):
        total = total + item
        print(f"Added {item}. Total is now: {total}")
    else:
        print(f"Ignored non-numeric or boolean item: {item}")

print(f"Corrected total after Step 4: {total}")

# What we accomplished in this step:
# - We discovered that booleans are treated as integers by `isinstance()`.
# - We refined our logic with the `not` operator to explicitly ignore boolean values.


# Step 5
# Explanation: Let's consolidate everything into a clean script. We will process 
# the sample mixed list, display each item with its type, and clearly show the 
# final numeric sum without the booleans interfering.

# Test our code:
print("\n--- Step 5: Final Clean Script Demonstration ---")

mixed_data = [10, "Python", 5.5, False, True, 100, "Code", -2.5]
numeric_sum = 0

print("Processing mixed data list:")
for item in mixed_data:
    item_type = type(item).__name__
    
    if isinstance(item, (int, float)) and not isinstance(item, bool):
        numeric_sum += item
        print(f"[NUMBER] Added {item:5} (Type: {item_type})")
    else:
        print(f"[ IGNORE] Skipped {str(item):5} (Type: {item_type})")

print("-" * 40)
print(f"Final Valid Numeric Sum: {numeric_sum}")
# Expected output for Final Valid Numeric Sum: 113.0 
# (10 + 5.5 + 100 + -2.5)

# What we accomplished in this step:
# - We created a robust, production-ready loop for filtering and accumulating mixed data.
# - We used `type(item).__name__` to print a cleaner version of the type name.
# - We verified our code behaves exactly as expected with a clear test demonstration.


# CONGRATULATIONS! 🎉
# You have successfully written a program that intelligently processes lists of 
# mixed data types! You learned how to use `type()` to inspect variables and 
# `isinstance()` to filter data robustly. Most importantly, you navigated the 
# tricky Python quirk where booleans act as integers, learning how to exclude 
# them properly when accumulating sums.
# Try modifying the starting list with your own data combinations to see how the code handles it.
# Remember: The best way to learn is by doing! 🚀
