"""Question: Explore mutability, copying, and identity with Python's data types. Demonstrate shallow copying vs deep copying of nested lists, show how changing a mutable object affects all references to it, and use the `copy` module to create independent copies."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Familiarize yourself with the `copy` module by importing it.
# - Understand that a simple assignment (using `=`) creates a reference to the same object, not a new copy.
# - Notice how nested structures (like a list inside a list) require a deep copy to become truly independent.
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Try creating a nested list like `original = [[1, 2], [3, 4]]`.
# - Assign `shallow = original` and observe that both variables refer to the same object (`is` returns True).
# - Use `shallow = original.copy()` or `list(original)` to create a shallow copy. Notice that the outer list is new, but the inner lists are still shared!
# - Import `copy` and use `copy.deepcopy(original)` to create a fully independent copy.
# - Test by modifying inner lists and seeing which versions are affected.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by creating a nested list and assigning it to a new 
# variable using the `=` operator. In Python, this doesn't copy the list; it just 
# creates a new label pointing to the exact same object in memory. We can prove 
# this using the `is` operator and by modifying one list to see the other change.

original = [[1, 2], [3, 4]]
reference = original

print("--- Step 1: Assignment (=) ---")
print(f"Are they the exact same object? {original is reference}")

# Let's modify the reference
reference[0][0] = 99

print(f"Original after reference changed: {original}")
print(f"Reference after change: {reference}\n")

# What we accomplished in this step:
# - We created a nested list.
# - We used assignment to create a second reference to the same list.
# - We demonstrated that modifying the reference also modifies the original.


# Step 2
# Explanation: To avoid the issue in Step 1, we might try using the `.copy()` 
# method. This creates a "shallow copy". It creates a brand-new outer list, but 
# it fills that new list with references to the original inner objects. Let's see 
# what happens when we modify an inner list.

original = [[1, 2], [3, 4]]
reference = original
reference[0][0] = 99

# Resetting original for Step 2 demonstration
original_two = [[1, 2], [3, 4]]
shallow = original_two.copy()

print("--- Step 2: Shallow Copy (.copy()) ---")
print(f"Is outer list the same object? {original_two is shallow}")
print(f"Is inner list the same object? {original_two[0] is shallow[0]}")

# Let's modify an inner list in the shallow copy
shallow[1][0] = 88

print(f"Original two after shallow inner change: {original_two}")
print(f"Shallow copy after change: {shallow}\n")

# What we accomplished in this step:
# - We used `.copy()` to create a shallow copy.
# - We proved the outer lists are independent (`is` returned False).
# - We saw that modifying a nested list still affects both variables because the inner references are shared.


# Step 3
# Explanation: To create a completely independent copy of a nested structure, we 
# need to use the `copy` module and its `deepcopy()` function. This recursively 
# copies every object it finds, ensuring nothing is shared.

import copy

original = [[1, 2], [3, 4]]
reference = original
reference[0][0] = 99

original_two = [[1, 2], [3, 4]]
shallow = original_two.copy()
shallow[1][0] = 88

# Resetting original for Step 3 demonstration
original_three = [[1, 2], [3, 4]]
deep = copy.deepcopy(original_three)

print("--- Step 3: Deep Copy (deepcopy()) ---")
print(f"Is outer list the same object? {original_three is deep}")
print(f"Is inner list the same object? {original_three[0] is deep[0]}")

# Let's modify an inner list in the deep copy
deep[0][1] = 77

print(f"Original three after deep inner change: {original_three}")
print(f"Deep copy after change: {deep}\n")

# What we accomplished in this step:
# - We imported the `copy` module.
# - We used `copy.deepcopy()` to create a fully independent clone.
# - We verified that inner modifications do not affect the original object.


# Step 4
# Explanation: Let's summarize what we've learned by printing a clean table to 
# the console. This will help reinforce the differences between assignment, 
# shallow copying, and deep copying.

import copy

original = [[1, 2], [3, 4]]
reference = original
reference[0][0] = 99

original_two = [[1, 2], [3, 4]]
shallow = original_two.copy()
shallow[1][0] = 88

original_three = [[1, 2], [3, 4]]
deep = copy.deepcopy(original_three)
deep[0][1] = 77

print("--- Step 4: Summary Table ---")
print("Method             | Outer Independent? | Inner Independent?")
print("-" * 60)
print("Assignment (=)     | No                 | No")
print("Shallow Copy       | Yes                | No")
print("Deep Copy          | Yes                | Yes\n")

# What we accomplished in this step:
# - We consolidated our findings into an easy-to-read reference table.


# Step 5
# Explanation: Now we'll consolidate all three approaches into a single, clean 
# script. We will organize our test block clearly, running all three scenarios 
# from a fresh original list each time to see the behavior exactly as expected.

import copy

# Test our code:
print("--- EXPERT DATA TYPES: MUTABILITY AND COPYING ---")

# Scenario 1: Assignment
print("\n1. ASSIGNMENT (=)")
list_a = [[1, 2], [3, 4]]
list_b = list_a
list_b[0][0] = "MODIFIED"

print(f"Original : {list_a}")
# Expected: [['MODIFIED', 2], [3, 4]]
print(f"Assigned : {list_b}")
# Expected: [['MODIFIED', 2], [3, 4]]


# Scenario 2: Shallow Copy
print("\n2. SHALLOW COPY (.copy())")
list_c = [[1, 2], [3, 4]]
list_d = list_c.copy()
# Modifying inner list
list_d[0][0] = "MODIFIED"
# Modifying outer list (adding new element)
list_d.append([5, 6])

print(f"Original : {list_c}")
# Expected: [['MODIFIED', 2], [3, 4]] (Inner list changed, but no new element appended)
print(f"Shallow  : {list_d}")
# Expected: [['MODIFIED', 2], [3, 4], [5, 6]]


# Scenario 3: Deep Copy
print("\n3. DEEP COPY (copy.deepcopy())")
list_e = [[1, 2], [3, 4]]
list_f = copy.deepcopy(list_e)
list_f[0][0] = "MODIFIED"

print(f"Original : {list_e}")
# Expected: [[1, 2], [3, 4]] (Completely untouched)
print(f"Deep     : {list_f}")
# Expected: [['MODIFIED', 2], [3, 4]]

# What we accomplished in this step:
# - We built a comprehensive test script demonstrating the three types of variable assignment and copying.
# - We documented the expected outputs directly in the code comments for easy validation.


# CONGRATULATIONS! 🎉
# You have tackled one of the most common stumbling blocks in Python: mutability and references!
# You now understand that `=` simply points a new name to the same object in memory.
# You also learned the crucial difference between a shallow copy (which only copies the outer container) 
# and a deep copy (which recursively copies everything inside).
# Understanding these concepts will save you from countless debugging headaches in the future.
# Remember: The best way to learn is by doing! 🚀
