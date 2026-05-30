"""Question: Implement the bubble sort algorithm to sort a list of numbers in ascending order. The algorithm should repeatedly step through the list, compare adjacent elements, and swap them if they are in the wrong order. Demonstrate the sorting process on a sample list."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Think about using nested loops: an outer loop to track passes, and an inner loop to step through the list.
# - In the inner loop, you will need to compare adjacent pairs (current element and the next element).
# - If the current element is greater than the next element, you will need to swap them.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use an outer loop that iterates over the list multiple times (one pass for each element).
# - Use an inner loop that goes from the start to the unsorted portion of the list.
# - Compare `list[j]` and `list[j+1]`; if they are in the wrong order, swap them.
# - To swap in Python, use `a, b = b, a`.
# - Optionally add a flag to stop early if a pass makes no swaps (the list is already sorted).
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by defining our function and setting up the basic loop 
# structure. Bubble sort requires nested loops. The outer loop ensures we do enough 
# passes to sort the whole list. The inner loop walks through the list and looks at 
# adjacent elements. For now, we will simply print the pairs we are about to compare 
# so we can visualize how the inner loop works. Note that our inner loop stops at 
# `n - 1` so we don't get an IndexError when looking at `j + 1`.

def bubble_sort(data):
    n = len(data)
    # The outer loop dictates how many passes we make
    for i in range(n):
        # The inner loop iterates through the list, comparing adjacent items
        for j in range(0, n - 1):
            print(f"We would compare {data[j]} and {data[j+1]}")

# What we accomplished in this step:
# - Created the `bubble_sort` function signature.
# - Set up the nested loops required for the algorithm.
# - Identified the boundaries for the inner loop to prevent out-of-bounds errors.


# Step 2
# Explanation: Now we'll replace the print statement with actual logic. We want to 
# compare `data[j]` with `data[j+1]`. If the left element is larger than the right 
# element, they are out of order, and we must swap them. Python makes swapping easy 
# with the syntax `a, b = b, a`. We will also optimize the inner loop a bit: after 
# every full pass, the largest remaining element "bubbles" up to its correct position 
# at the end. So, we don't need to check the last `i` elements anymore! We'll change 
# the inner loop bound to `n - i - 1`. Finally, let's print the list after each 
# pass to see the progress.

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        # We subtract 'i' because the last 'i' elements are already sorted
        for j in range(0, n - i - 1):
            if data[j] > data[j+1]:
                # Swap the elements
                data[j], data[j+1] = data[j+1], data[j]
                
        print(f"List after pass {i + 1}: {data}")

# What we accomplished in this step:
# - Implemented the comparison logic for adjacent elements.
# - Added the tuple-unpacking syntax to safely swap values in place.
# - Optimized the inner loop boundary to avoid unnecessary comparisons.
# - Added a print statement to observe the list getting sorted pass by pass.


# Step 3
# Explanation: Our algorithm works, but there is a common optimization we can add. 
# What if the list gets completely sorted before the outer loop finishes? We would 
# be doing unnecessary passes! We can add a `swapped` flag. We set it to False at 
# the start of each outer loop iteration. If we ever make a swap, we change it to 
# True. If we make it through an entire pass without a single swap, the list is 
# fully sorted, and we can `break` out early.

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                
        # If no elements were swapped in this pass, the list is already sorted!
        if not swapped:
            break

# What we accomplished in this step:
# - Introduced a `swapped` boolean flag to track state during each pass.
# - Added logic to exit the sorting process early if the list is completely sorted.


# Step 4
# Explanation: Let's clean up our code into a final, professional function. We'll 
# remove the debugging print statements so the function simply performs the sort 
# silently. Because lists are mutable in Python, sorting happens "in-place" 
# (modifying the original list directly), but returning the sorted list is also a 
# nice convenience.

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                
        if not swapped:
            break
            
    return data

# What we accomplished in this step:
# - Finalized a clean, optimized bubble sort function.
# - Confirmed the function returns the gracefully sorted list.


# Step 5
# Explanation: Our bubble sort implementation is complete. Now we will create a 
# test block to demonstrate how it works in practice. We will define a messy, 
# unsorted list, print its original state, run our function, and then print the 
# newly sorted list to verify everything works perfectly.

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            break
    return data


# Test our bubble sort:
if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original list:")
    print(sample_list)
    # Expected output: [64, 34, 25, 12, 22, 11, 90]
    
    # Sort the list using our function
    sorted_list = bubble_sort(sample_list)
    
    print("\nSorted list:")
    print(sorted_list)
    # Expected output: [11, 12, 22, 25, 34, 64, 90]


# CONGRATULATIONS! 🎉
# You've successfully implemented one of the classic computer science sorting algorithms!
#
# Key takeaways:
# - Bubble Sort Mechanism: You learned how larger elements "bubble" to the top (end) of the list one by one.
# - Nested Loops: You saw how two loops work together—one for passes, and one for iterating through elements.
# - Swapping: You mastered modifying elements in place without needing a separate temporary list.
# - Time Complexity: You observed an O(n²) time complexity algorithm. For a large list, nested loops mean the number of operations grows quadratically!
# - Optional Optimization: You implemented a neat flag (`swapped`) to stop the algorithm gracefully when it finishes early.
#
# Remember: The best way to learn is by doing! 🚀
