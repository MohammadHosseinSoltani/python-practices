"""Question: Investigate how Python handles variable assignment and identity. Compare mutable and immutable objects, explore the difference between `is` and `==`, and practice choosing meaningful variable names."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Think about using the built-in `id()` function to peek "under the hood" at where objects live in memory.
# - Remember that testing equality (do they look the same?) is different from testing identity (are they literally the exact same object?).
# - Observe how lists (which are mutable) behave very differently from integers (which are immutable) when you try to change them.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use the `id()` function to see the memory address of an object.
# - Use `==` to check if values are equal, and `is` to check if two variables point to the exact same object.
# - Try modifying a list through one variable and see if another variable pointing to the same list sees the change.
# - Remember that integers, floats, and strings are immutable; when you 'change' them, you actually create a new object.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by exploring "immutable" objects, like integers. When we assign 
# a number to a variable, Python creates an object in memory. If we assign that variable 
# to a second variable, both point to the exact same object. We can prove this using the 
# `id()` function, which returns the object's unique memory address. However, integers 
# cannot be changed. If we "modify" the first variable, Python actually creates a brand 
# new object in a new memory location! Let's see this in action.

a = 10
b = a

print("--- Immutability (Integers) ---")
print(f"Initial: a = {a}, b = {b}")
print(f"ID of a: {id(a)}")
print(f"ID of b: {id(b)}")
print("Are they the same object?", a is b)

# Now let's try to "change" a
a = a + 5

print("\nAfter adding 5 to a:")
print(f"a = {a}, b = {b}")
print(f"New ID of a: {id(a)}")
print(f"ID of b: {id(b)}")
print("Are they the same object now?", a is b)

# What we accomplished in this step:
# - Used `id()` to inspect memory addresses.
# - Demonstrated that assigning one variable to another makes them share the same object.
# - Proved that "modifying" an immutable integer actually points the variable to a completely new object, leaving the original intact.


# Step 2
# Explanation: Now let's look at "mutable" objects, like lists. Because lists can be 
# changed in place, they behave very differently. If we assign a list to `list_x`, and 
# then set `list_y = list_x`, they both point to the same object. If we modify the list 
# (like appending an item), *both* variables will reflect the change because the underlying 
# object itself was modified, not replaced.

a = 10
b = a
a = a + 5

print("\n--- Mutability (Lists) ---")
list_x = [1, 2, 3]
list_y = list_x

print(f"Initial lists: list_x = {list_x}, list_y = {list_y}")
print(f"ID of list_x: {id(list_x)}")
print(f"ID of list_y: {id(list_y)}")

# Now we modify list_x in place
list_x.append(4)

print("\nAfter appending 4 to list_x:")
print(f"list_x = {list_x}")
print(f"list_y = {list_y}")  # Notice list_y changed too!
print(f"ID of list_x: {id(list_x)}")
print(f"ID of list_y: {id(list_y)}")

# What we accomplished in this step:
# - Created a list and created a second reference to it.
# - Demonstrated that mutating a list affects all variables that point to that list.
# - Showed that the `id()` remains exactly the same even after the list's contents change.


# Step 3
# Explanation: This leads us to a critical distinction in Python: equality (`==`) versus 
# identity (`is`). `==` asks "Do these objects have the same value?", while `is` asks 
# "Are these the exact same object in memory?". Let's create two identical lists 
# independently. They will have the same values, but they will be two distinct objects.

a = 10
b = a
a = a + 5

list_x = [1, 2, 3]
list_y = list_x
list_x.append(4)

print("\n--- Equality (==) vs Identity (is) ---")
# Create two independent lists with identical contents
list_one = ["apple", "banana"]
list_two = ["apple", "banana"]

print(f"list_one: {list_one}")
print(f"list_two: {list_two}")

# Do they have the same values?
print(f"list_one == list_two : {list_one == list_two}")

# Are they the same exact object in memory?
print(f"list_one is list_two : {list_one is list_two}")

# What we accomplished in this step:
# - Highlighted the difference between the `==` operator and the `is` keyword.
# - Showed how two variables can be completely equal in value, yet distinct in identity.


# Step 4
# Explanation: Now that we understand how variables work under the hood, let's talk 
# about how we name them. Good variable naming is crucial for code readability. 
# Let's look at a bad example calculating the area of a circle, and then refactor 
# it using descriptive names. Note how much easier the second version is to understand 
# without needing any comments!

a = 10
b = a
a = a + 5

list_x = [1, 2, 3]
list_y = list_x
list_x.append(4)

list_one = ["apple", "banana"]
list_two = ["apple", "banana"]

print("\n--- Variable Naming Best Practices ---")

# BAD NAMING: Cryptic and hard to read
r = 5
p = 3.14159
a_c = p * (r ** 2)
print(f"Bad naming result: {a_c}")

# GOOD NAMING: Descriptive and self-documenting
circle_radius = 5
pi_value = 3.14159
circle_area = pi_value * (circle_radius ** 2)
print(f"Good naming result: {circle_area}")

# What we accomplished in this step:
# - Demonstrated the pitfalls of using single-letter or cryptic variable names.
# - Applied `snake_case` best practices to create readable, self-documenting code.


# Step 5
# Explanation: We have covered a lot of advanced variable concepts! Let's clean up our 
# script into a cohesive final version. We will format the output clearly and include 
# the expected results as comments. This will serve as an excellent reference file 
# for how Python manages data in memory.

# Test our code:
if __name__ == "__main__":
    
    print("--- Immutability (Integers) ---")
    score_a = 100
    score_b = score_a
    print(f"Before change: score_a = {score_a}, score_b = {score_b} | Same object? {score_a is score_b}")
    score_a += 50
    print(f"After change : score_a = {score_a}, score_b = {score_b} | Same object? {score_a is score_b}")
    # Expected: Before change they are the same object (True). After adding 50, score_a points to a new object, so they are not the same (False).
    
    print("\n--- Mutability (Lists) ---")
    team_a = ["Alice", "Bob"]
    team_b = team_a
    print(f"Before append: team_a = {team_a}, team_b = {team_b}")
    team_a.append("Charlie")
    print(f"After append : team_a = {team_a}, team_b = {team_b}")
    # Expected: Both lists will show ["Alice", "Bob", "Charlie"] because they point to the exact same mutable object.
    
    print("\n--- Equality (==) vs Identity (is) ---")
    cart_one = ["shoes", "shirt"]
    cart_two = ["shoes", "shirt"]
    print(f"cart_one == cart_two (Equal values?)  : {cart_one == cart_two}")
    print(f"cart_one is cart_two (Same identity?) : {cart_one is cart_two}")
    # Expected: Equal values? True. Same identity? False.
    
    print("\n--- Variable Naming Best Practices ---")
    celsius_temperature = 25
    fahrenheit_temperature = (celsius_temperature * 9/5) + 32
    print(f"{celsius_temperature}°C is equal to {fahrenheit_temperature}°F.")
    # Expected: 25°C is equal to 77.0°F. (Using descriptive names makes the formula obvious!)


# CONGRATULATIONS! 🎉
# You've taken a deep dive into the mechanics of Python variables!
#
# Key takeaways:
# - Object Identity: Variables are just nametags pointing to objects in memory. You can use `id()` to see exactly where they point.
# - Mutability vs Immutability: You saw how modifying an integer creates a new object, while modifying a list alters the existing object in place.
# - `is` vs `==`: You learned that identical values do not necessarily mean identical objects. `==` checks value, `is` checks memory address.
# - Variable Naming Best Practices: You practiced writing self-documenting code using descriptive `snake_case` names.
#
# Remember: The best way to learn is by doing! 🚀
