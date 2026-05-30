"""Question: Implement linear search to find a target value in a list. The function should return the index of the target if found, or -1 if not found. Demonstrate it with a sample list."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Think about looping through the list one element at a time from start to finish.
# - Keep track of the current index as you examine each item.
# - Return the index immediately when the target value is found.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use a `for` loop with `enumerate()` to get both the index and value as you traverse the list.
# - If the current element matches the target, return the current index immediately.
# - If the loop finishes without finding the target, return -1.
# - Test with a small list and a few different target values, including values not present.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by defining our function signature. A linear search needs 
# two things: the list of data to search through, and the target value we want to find. 
# We will use a `for` loop with Python's built-in `enumerate()` function. This allows 
# us to easily look at both the index and the value at the same time. For now, let's 
# just print each element to see how the traversal works.

def linear_search(data_list, target):
    for index, value in enumerate(data_list):
        print(f"Checking index {index}: value is {value}")

# What we accomplished in this step:
# - Defined the `linear_search` function with appropriate parameters.
# - Used `enumerate()` to loop through the list, giving us access to both index and value.
# - Added a temporary print statement to visualize the sequential traversal.


# Step 2
# Explanation: Now we'll add the actual search logic. Instead of just printing the 
# values, we want to compare each `value` to our `target`. If they match, we have 
# successfully found what we are looking for! Because the problem asks for the index 
# where the target is located, we will return the `index` immediately. This is known 
# as an "early return" and it stops the loop from doing unnecessary extra work.

def linear_search(data_list, target):
    for index, value in enumerate(data_list):
        # Compare the current value to the target
        if value == target:
            # Target found! Return its position immediately.
            return index

# What we accomplished in this step:
# - Added an `if` statement to compare each element against the target.
# - Implemented an early return to stop the function as soon as the target is found.


# Step 3
# Explanation: Our function works great if the target is actually in the list. But 
# what happens if it isn't? If the loop finishes checking every single item and never 
# triggers the `return index` statement, it will exit the loop. At this point, we 
# know for a fact the target does not exist in the list. We will handle this by 
# returning -1 at the very end of the function.

def linear_search(data_list, target):
    for index, value in enumerate(data_list):
        if value == target:
            return index
            
    # If the loop finishes without returning, the target is not in the list
    return -1

# What we accomplished in this step:
# - Handled the "not found" edge case by returning -1 after the loop completes.
# - Finalized the core algorithm for linear search.


# Step 4
# Explanation: Let's demonstrate our function in action. We will create a sample list 
# of numbers and call our `linear_search` function a couple of times: once for a 
# number we know is in the list, and once for a number that isn't. We'll print the 
# results to verify our logic works correctly.

def linear_search(data_list, target):
    for index, value in enumerate(data_list):
        if value == target:
            return index
    return -1

if __name__ == "__main__":
    sample_list = [10, 23, 45, 70, 11, 15]
    
    # Searching for an existing target
    result_found = linear_search(sample_list, 70)
    print("Index of 70:", result_found)
    
    # Searching for a non-existing target
    result_missing = linear_search(sample_list, 99)
    print("Index of 99:", result_missing)

# What we accomplished in this step:
# - Set up a sample list of integers.
# - Called our function with both an existing and a non-existing target.
# - Printed the return values to test our implementation.


# Step 5
# Explanation: Our algorithm is complete and tested! Let's clean up our script into 
# a final, consolidated version. We will format our test outputs nicely and include 
# comments showing the expected results so anyone running this file knows exactly 
# what should happen.

def linear_search(data_list, target):
    for index, value in enumerate(data_list):
        if value == target:
            return index
    return -1


# Test our linear search:
if __name__ == "__main__":
    my_numbers = [4, 8, 15, 16, 23, 42]
    print(f"Searching through the list: {my_numbers}")
    
    print("\n1. Searching for target 16:")
    index_16 = linear_search(my_numbers, 16)
    print(f"Target 16 found at index: {index_16}")
    # Expected output: Target 16 found at index: 3
    
    print("\n2. Searching for target 4:")
    index_4 = linear_search(my_numbers, 4)
    print(f"Target 4 found at index: {index_4}")
    # Expected output: Target 4 found at index: 0
    
    print("\n3. Searching for target 100:")
    index_100 = linear_search(my_numbers, 100)
    print(f"Target 100 found at index: {index_100}")
    # Expected output: Target 100 found at index: -1

# What we accomplished in this step:
# - Consolidated the code into a clean, professional script.
# - Created a comprehensive test block demonstrating successful hits at different positions and a clear miss.
# - Documented the expected outputs using comments.


# CONGRATULATIONS! 🎉
# You've successfully implemented the linear search algorithm!
#
# Key takeaways:
# - Sequential Search: You learned how to traverse a data structure one element at a time from start to finish.
# - Early Return Pattern: You saw how returning a value immediately from inside a loop saves processing time.
# - Time Complexity: You observed an algorithm with O(n) time complexity. If the list has 1,000,000 items, and the target is at the very end (or not there at all), the computer has to perform 1,000,000 checks!
#
# Try extending this by creating a linear search that returns a list of *all* indices where a duplicate target might appear!
# Remember: The best way to learn is by doing! 🚀
