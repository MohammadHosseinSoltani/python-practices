"""Question: Implement a simple dynamic array (list-like structure) from scratch. It should support appending, inserting, deleting, and accessing elements, and should resize itself automatically when full."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Think about using a standard Python list as your underlying static storage (e.g., initialized with a fixed size of Nones).
# - Keep track of both the 'size' (how many items are currently in your array) and the 'capacity' (how many items it can hold before needing to grow).
# - Write discrete methods for each operation: append, insert, get, and delete.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use a Python list to store elements internally (e.g., self.data = [None] * capacity).
# - Keep track of self.size (number of actual elements) and self.capacity (total slots available).
# - When appending, if the array is full, double the capacity by creating a new, larger list and copying elements over.
# - Implement methods: append(item), insert(index, item), delete(index), and get(index).
# - Test each operation step by step.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by setting up our DynamicArray class. Under the hood, dynamic
# arrays use a fixed-size block of memory. In Python, we will simulate this by creating a 
# list of a specific capacity filled with `None`. We also need to track the `capacity` 
# (total slots) and `size` (number of actual elements currently stored). Finally, we will 
# add a helper method `__str__` so we can easily view the contents of our array.

class DynamicArray:
    def __init__(self, capacity=1):
        # We start with a very small capacity to demonstrate resizing later
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity
        
    def __str__(self):
        # We only want to show the actual elements, not the empty (None) slots
        actual_elements = self.data[:self.size]
        return f"[{', '.join(str(item) for item in actual_elements)}]"

# What we accomplished in this step:
# - Created the basic class structure.
# - Initialized internal storage using a fixed-size list.
# - Set up tracking for both capacity and current size.
# - Implemented a string representation for easy testing.


# Step 2
# Explanation: Now we will implement the `append` method, which adds an item to the end 
# of the array. But what happens if the array is full (size == capacity)? We need to 
# implement a private `_resize` method that creates a new, larger array (usually double 
# the size), copies the old elements over, and updates our internal references.

class DynamicArray:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity
        
    def __str__(self):
        actual_elements = self.data[:self.size]
        return f"[{', '.join(str(item) for item in actual_elements)}]"
        
    def _resize(self):
        # Double the capacity
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity
        
        # Copy existing elements to the new array
        for i in range(self.size):
            new_data[i] = self.data[i]
            
        # Update our internal references
        self.data = new_data
        self.capacity = new_capacity
        
    def append(self, item):
        # Check if there is space; if not, resize
        if self.size == self.capacity:
            self._resize()
            
        # Add the new item at the first available empty slot
        self.data[self.size] = item
        self.size += 1

# What we accomplished in this step:
# - Added a `_resize` method to dynamically grow our internal storage.
# - Implemented `append` to add items, automatically resizing when necessary.


# Step 3
# Explanation: Let's add the ability to retrieve an element at a specific index. We 
# must ensure the requested index is valid (bounds checking) before returning the value.

class DynamicArray:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity
        
    def __str__(self):
        actual_elements = self.data[:self.size]
        return f"[{', '.join(str(item) for item in actual_elements)}]"
        
    def _resize(self):
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
        
    def append(self, item):
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = item
        self.size += 1
        
    def get(self, index):
        # Ensure the index is within the bounds of our actual stored elements
        if not (0 <= index < self.size):
            raise IndexError("Array index out of bounds")
        return self.data[index]

# What we accomplished in this step:
# - Implemented `get` to safely retrieve elements by index.
# - Added crucial bounds checking to prevent invalid memory access.


# Step 4
# Explanation: Next, we'll implement `insert`, which places an item at a specific index.
# This operation requires shifting all elements from that index onward to the right 
# to make room. If the array is full, we must also resize it first.

class DynamicArray:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity
        
    def __str__(self):
        actual_elements = self.data[:self.size]
        return f"[{', '.join(str(item) for item in actual_elements)}]"
        
    def _resize(self):
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
        
    def append(self, item):
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = item
        self.size += 1
        
    def get(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Array index out of bounds")
        return self.data[index]
        
    def insert(self, index, item):
        # We can insert anywhere up to self.size (which is equivalent to append)
        if not (0 <= index <= self.size):
            raise IndexError("Array index out of bounds")
            
        if self.size == self.capacity:
            self._resize()
            
        # Shift elements right, starting from the end down to the target index
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
            
        # Insert the new item
        self.data[index] = item
        self.size += 1

# What we accomplished in this step:
# - Implemented `insert` to add items at specific indices.
# - Added logic to shift existing elements to the right to prevent overwriting.


# Step 5
# Explanation: Finally, we need a way to remove elements. The `delete` method removes
# an item at a specific index and shifts all subsequent elements to the left to fill the gap.

class DynamicArray:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity
        
    def __str__(self):
        actual_elements = self.data[:self.size]
        return f"[{', '.join(str(item) for item in actual_elements)}]"
        
    def _resize(self):
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
        
    def append(self, item):
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = item
        self.size += 1
        
    def get(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Array index out of bounds")
        return self.data[index]
        
    def insert(self, index, item):
        if not (0 <= index <= self.size):
            raise IndexError("Array index out of bounds")
            
        if self.size == self.capacity:
            self._resize()
            
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
            
        self.data[index] = item
        self.size += 1
        
    def delete(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Array index out of bounds")
            
        # Shift elements left to overwrite the deleted item
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
            
        # Clear the last element and decrease size
        self.data[self.size - 1] = None
        self.size -= 1

# What we accomplished in this step:
# - Implemented `delete` to remove items by index.
# - Added logic to shift elements to the left, closing the gap left by the deleted item.


# Step 6
# Explanation: Now we have a fully functional dynamic array! Let's write a test script 
# to demonstrate appending, getting, inserting, and deleting items, while also observing
# how the internal capacity grows.

class DynamicArray:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity
        
    def __str__(self):
        actual_elements = self.data[:self.size]
        return f"[{', '.join(str(item) for item in actual_elements)}]"
        
    def _resize(self):
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
        
    def append(self, item):
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = item
        self.size += 1
        
    def get(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Array index out of bounds")
        return self.data[index]
        
    def insert(self, index, item):
        if not (0 <= index <= self.size):
            raise IndexError("Array index out of bounds")
            
        if self.size == self.capacity:
            self._resize()
            
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
            
        self.data[index] = item
        self.size += 1
        
    def delete(self, index):
        if not (0 <= index < self.size):
            raise IndexError("Array index out of bounds")
            
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
            
        self.data[self.size - 1] = None
        self.size -= 1


# Test our dynamic array:
if __name__ == "__main__":
    print("Initializing DynamicArray with capacity 1...")
    arr = DynamicArray()
    print(f"Array: {arr} | Size: {arr.size} | Capacity: {arr.capacity}")
    # Expected: Array: [] | Size: 0 | Capacity: 1
    
    print("\nAppending items: 10, 20, 30...")
    arr.append(10)
    arr.append(20)
    arr.append(30)
    print(f"Array: {arr} | Size: {arr.size} | Capacity: {arr.capacity}")
    # Expected: Array: [10, 20, 30] | Size: 3 | Capacity: 4
    
    print("\nGetting item at index 1...")
    print(f"Item at index 1 is: {arr.get(1)}")
    # Expected: Item at index 1 is: 20
    
    print("\nInserting 15 at index 1...")
    arr.insert(1, 15)
    print(f"Array: {arr} | Size: {arr.size} | Capacity: {arr.capacity}")
    # Expected: Array: [10, 15, 20, 30] | Size: 4 | Capacity: 4
    
    print("\nDeleting item at index 2 (which is 20)...")
    arr.delete(2)
    print(f"Array: {arr} | Size: {arr.size} | Capacity: {arr.capacity}")
    # Expected: Array: [10, 15, 30] | Size: 3 | Capacity: 4


# CONGRATULATIONS! 🎉
# You've just built one of the most fundamental data structures from scratch!
# 
# Key takeaways:
# - Dynamic Resizing: You learned how dynamic arrays hide the complexity of fixed memory allocation by transparently resizing themselves.
# - Time Complexity Intuition: You saw firsthand how appending is usually fast O(1), but sometimes requires an O(N) resize.
# - Shifting Elements: You implemented the O(N) operations of inserting and deleting, which require shifting subsequent elements.
#
# Try extending this class by adding methods like `pop()` (remove from the end), `remove(value)` (find and delete a specific value), or shrinking the array when it becomes mostly empty.
#
# Remember: The best way to learn is by doing! 🚀
