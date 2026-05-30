"""Question: Implement a Stack class from scratch using a Python list as the underlying storage. The stack should support push, pop, peek, and checking if it is empty."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - A stack follows the Last-In-First-Out (LIFO) principle. Think of a stack of plates!
# - You can use a standard Python list as your underlying storage to hold the elements.
# - Make sure to handle edge cases, like what happens if someone tries to pop or peek from an empty stack.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use a Python list (e.g., self.items = []) to store the stack elements.
# - push(item) adds to the end of the list: self.items.append(item).
# - pop() removes and returns the last item, but only if the stack is not empty. Otherwise, raise an appropriate error.
# - peek() returns the last item without removing it, with an empty-check as well.
# - is_empty() simply checks if the list is empty.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by defining our Stack class. Under the hood, we will use 
# a standard Python list to store our items. We will also add a simple helper method 
# called `is_empty()` to check if the stack currently has any elements.

class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        # Returns True if the list has a length of 0, False otherwise
        return len(self.items) == 0

# What we accomplished in this step:
# - Created the `Stack` class.
# - Initialized an empty list `self.items` to act as our underlying storage.
# - Added an `is_empty()` method to easily check the stack's state.


# Step 2
# Explanation: Now we'll add the `push` method. Since a stack is LIFO (Last-In, 
# First-Out), adding an item to the "top" of the stack is conceptually identical 
# to appending an item to the end of our list.

class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def push(self, item):
        self.items.append(item)

# What we accomplished in this step:
# - Implemented `push(item)` using the built-in list `append()` method.


# Step 3
# Explanation: Let's implement `peek()`. This method allows us to look at the top 
# item of the stack without removing it. However, if the stack is empty, there is 
# nothing to look at! We must check if the stack is empty first, and if it is, 
# raise an IndexError to let the user know they've made an invalid operation.

class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def push(self, item):
        self.items.append(item)
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek from an empty stack")
        # Return the last item in the list
        return self.items[-1]

# What we accomplished in this step:
# - Implemented `peek()` to view the top element.
# - Added crucial error handling for the empty stack scenario.


# Step 4
# Explanation: Next up is `pop()`. This method removes the top item from the stack 
# and returns it to the user. Just like `peek()`, we need to ensure the stack isn't 
# empty before trying to remove an element. We can use Python's built-in `pop()` 
# list method to do the heavy lifting for us.

class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def push(self, item):
        self.items.append(item)
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek from an empty stack")
        return self.items[-1]
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        # Remove and return the last item in the list
        return self.items.pop()

# What we accomplished in this step:
# - Implemented `pop()` to remove and return the top element.
# - Protected the operation with an empty-check to prevent unexpected crashes.


# Step 5
# Explanation: It is often useful to know exactly how many items are currently in 
# our stack. Let's add a quick `size()` method that returns the length of our 
# internal list.

class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def push(self, item):
        self.items.append(item)
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek from an empty stack")
        return self.items[-1]
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()
        
    def size(self):
        return len(self.items)

# What we accomplished in this step:
# - Added a `size()` method for convenience.


# Step 6
# Explanation: Our stack is now complete! Let's put all the pieces together into a 
# clean, final script and write a comprehensive test to verify that pushing, popping, 
# peeking, and checking the size all work seamlessly together.

class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def push(self, item):
        self.items.append(item)
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek from an empty stack")
        return self.items[-1]
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()
        
    def size(self):
        return len(self.items)


# Test our stack:
if __name__ == "__main__":
    my_stack = Stack()
    
    print("1. Is the stack empty?", my_stack.is_empty())
    # Expected: True
    
    print("\n2. Pushing 10, 20, and 30 onto the stack...")
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    
    print("3. What is the stack size?", my_stack.size())
    # Expected: 3
    
    print("4. Peeking at the top item:", my_stack.peek())
    # Expected: 30
    
    print("\n5. Popping the top item:", my_stack.pop())
    # Expected: 30
    
    print("6. Peeking at the new top item:", my_stack.peek())
    # Expected: 20
    
    print("7. What is the new stack size?", my_stack.size())
    # Expected: 2
    
    print("\n8. Popping remaining items...")
    print("Popped:", my_stack.pop())  # Expected: 20
    print("Popped:", my_stack.pop())  # Expected: 10
    
    print("9. Is the stack empty now?", my_stack.is_empty())
    # Expected: True


# CONGRATULATIONS! 🎉
# You have successfully implemented a Stack from scratch!
#
# Key takeaways:
# - LIFO Principle: You saw firsthand how a stack strictly follows Last-In-First-Out ordering.
# - Abstraction: Python lists are highly versatile, but by wrapping a list in a Stack class, we restricted how data can be interacted with to prevent logical bugs.
# - Error Handling: You learned the importance of predicting edge cases (like popping an empty stack) and raising helpful exceptions.
#
# Try extending this! Can you implement a Stack that only holds a maximum number of items? 
# Remember: The best way to learn is by doing! 🚀
