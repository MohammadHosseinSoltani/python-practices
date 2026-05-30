"""Question: Implement a singly linked list from scratch. It should support appending to the end, prepending to the beginning, deleting a node by value, and displaying the list."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Create a separate Node class to hold the data and a reference to the next node.
# - Your LinkedList class should maintain a reference to the 'head' (the first node).
# - Pay special attention to edge cases like an empty list or deleting the very first node.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Define a `Node` class with `data` and `next` attributes.
# - Define a `LinkedList` class with a `head` attribute, initially `None`.
# - For `append`, traverse to the end of the list, then link the new node.
# - For `prepend`, point the new node's `next` to the current head, then update head.
# - For `delete`, find the node before the target and adjust its `next` pointer.
# - Implement a `display` method to print all elements in order.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by creating the building block of our linked list: the Node. 
# A node is a simple object that holds some data and a pointer (or reference) to the 
# next node in the chain. When a node is created, it doesn't point to anything yet, 
# so `next` defaults to None.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)

# What we accomplished in this step:
# - Created the `Node` class.
# - Added an `__init__` method to store `data` and initialize a `next` pointer.
# - Implemented a simple string representation for easy printing later.


# Step 2
# Explanation: Now we'll create the LinkedList class to manage our nodes. It needs 
# a `head` attribute pointing to the first node. If the list is empty, `head` is None.
# We'll also add a `display` method to traverse the list, following the `next` 
# pointers until we reach the end, and print the contents. To ensure it works, we 
# will manually link a few nodes together and test it.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        # The list starts empty, so head is None
        self.head = None
        
    def display(self):
        elements = []
        current = self.head
        # Traverse the list until current becomes None (the end)
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty List")

# Test manually linking nodes:
if __name__ == "__main__":
    test_list = LinkedList()
    test_list.head = Node("A")
    test_list.head.next = Node("B")
    test_list.head.next.next = Node("C")
    test_list.display()
    # Expected output: A -> B -> C

# What we accomplished in this step:
# - Created the `LinkedList` class with a `head` attribute.
# - Implemented `display()` to traverse and print the nodes.
# - Tested our logic by manually creating and linking nodes.


# Step 3
# Explanation: Next, we add the `append` method to add a new node to the end of the list. 
# If the list is empty, the new node becomes the head. Otherwise, we must traverse 
# the entire list to find the last node (the one whose `next` is None) and attach 
# our new node there.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty List")
        
    def append(self, data):
        new_node = Node(data)
        
        # Case 1: The list is empty
        if self.head is None:
            self.head = new_node
            return
            
        # Case 2: The list has items, so traverse to the end
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            
        # Link the new node to the end
        last_node.next = new_node

# Test appending:
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.display()
    # Expected output: 10 -> 20 -> 30

# What we accomplished in this step:
# - Implemented the `append` method.
# - Handled the empty list edge case.
# - Wrote logic to traverse to the tail and link the new node.


# Step 4
# Explanation: Adding a node to the beginning is often called prepending. For `prepend`, 
# we create a new node, point its `next` to the current head, and then update the 
# head to be this new node. Notice how we don't need to traverse the list! This 
# is a fast, constant-time operation.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty List")
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def prepend(self, data):
        new_node = Node(data)
        # Point the new node to whatever is currently first
        new_node.next = self.head
        # Now make the new node the official head of the list
        self.head = new_node

# Test prepending:
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(20)
    my_list.prepend(10)
    my_list.prepend(5)
    my_list.display()
    # Expected output: 5 -> 10 -> 20

# What we accomplished in this step:
# - Implemented the `prepend` method.
# - Learned how to insert a node at the front of the list in O(1) time.


# Step 5
# Explanation: Deletion is the trickiest operation. We need to find the node with the 
# target value, but to remove it, we must change the `next` pointer of the *previous* 
# node so it skips over the target. We also have to handle special cases: what if 
# the list is empty? What if the node to delete is the head itself?

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty List")
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def delete(self, value):
        # Case 1: The list is empty
        if self.head is None:
            return
            
        # Case 2: The node to delete is the head
        if self.head.data == value:
            self.head = self.head.next
            return
            
        # Case 3: The node is somewhere else in the list
        current = self.head
        # Traverse, looking one step ahead so we can modify the current node's next pointer
        while current.next and current.next.data != value:
            current = current.next
            
        # If we found the value, skip over the node to delete it
        if current.next:
            current.next = current.next.next

# What we accomplished in this step:
# - Implemented the `delete` method.
# - Safely handled empty lists.
# - Correctly updated the head pointer when deleting the first element.
# - Maintained a reference to the previous node to bridge the gap during standard deletion.


# Step 6
# Explanation: We now have a complete Singly Linked List! Let's put everything together 
# in a clean, consolidated script and run a comprehensive test sequence to ensure all 
# our methods work harmoniously together.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty List")
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def delete(self, value):
        if self.head is None:
            print(f"Cannot delete {value}: List is empty.")
            return
            
        if self.head.data == value:
            self.head = self.head.next
            return
            
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
            
        if current.next:
            current.next = current.next.next
        else:
            print(f"Value {value} not found in the list.")


# Test our linked list:
if __name__ == "__main__":
    my_list = LinkedList()
    
    print("1. Initial display:")
    my_list.display()
    # Expected output: Empty List
    
    print("\n2. Appending 10, 20, 30:")
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.display()
    # Expected output: 10 -> 20 -> 30
    
    print("\n3. Prepending 5:")
    my_list.prepend(5)
    my_list.display()
    # Expected output: 5 -> 10 -> 20 -> 30
    
    print("\n4. Deleting middle element (20):")
    my_list.delete(20)
    my_list.display()
    # Expected output: 5 -> 10 -> 30
    
    print("\n5. Deleting head element (5):")
    my_list.delete(5)
    my_list.display()
    # Expected output: 10 -> 30
    
    print("\n6. Trying to delete a non-existent element (99):")
    my_list.delete(99)
    # Expected output: Value 99 not found in the list.


# CONGRATULATIONS! 🎉
# You have successfully built a Singly Linked List from scratch! 
#
# Key takeaways:
# - Nodes and Pointers: You learned how separate objects can be chained together using references (`next`).
# - Dynamic Memory: Unlike fixed arrays, linked lists can easily grow or shrink without needing to resize or shift memory blocks.
# - Traversal: You mastered writing `while` loops to walk through a data structure.
# - Edge Cases: You learned why the first element (`head`) often requires special handling.
#
# Remember: The best way to learn is by doing! 🚀
