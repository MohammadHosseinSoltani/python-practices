"""Question: Implement a Binary Search Tree (BST) from scratch. It should support inserting values, searching for a value, and performing an in-order traversal that prints all values in sorted order."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Think about creating a Node class first to represent each element and its left/right children.
# - Implementing recursive insertion is often easier: compare the new value with the current node, then traverse left if smaller, or right if larger.
# - Understanding the in-order traversal pattern (Left, Root, Right) is key to printing the values in sorted order.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Define a `Node` class with `value`, `left`, and `right` attributes.
# - Define a `BinarySearchTree` class with a `root` attribute, initially `None`.
# - For `insert`, recursively compare the new value with the current node: go left if smaller, right if larger.
# - For `search`, traverse the tree similarly, returning `True` if found, `False` if you hit a dead end.
# - For `in_order_traversal`, recursively visit left subtree, then the node itself, then right subtree.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by defining our Node class. In a binary tree, every node 
# contains some data (the value) and two pointers. One pointer links to the left child, 
# and the other links to the right child. When a node is newly created, it has no 
# children, so `left` and `right` default to None.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# What we accomplished in this step:
# - Created the `Node` class, the foundational building block of our tree.
# - Set up the `value`, `left`, and `right` attributes.


# Step 2
# Explanation: Now we'll create the BinarySearchTree class. It starts with a single 
# attribute, `root`, which points to the top node (None initially). We will also add 
# an `insert` method. If the tree is empty, the new node becomes the root. Otherwise, 
# we use a private helper method, `_insert`, to recursively travel down the tree. 
# If the value is smaller than the current node, we go left; if larger, we go right, 
# until we find an empty spot.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        # Case 1: The tree is completely empty
        if self.root is None:
            self.root = Node(value)
        else:
            # Case 2: We need to find the right spot, so we start at the root
            self._insert(value, self.root)
            
    def _insert(self, value, current_node):
        if value < current_node.value:
            # The value belongs on the left side
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            # The value belongs on the right side
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
        # Note: If value == current_node.value, we do nothing (no duplicates allowed)

# What we accomplished in this step:
# - Created the `BinarySearchTree` class and managed the root node.
# - Implemented the `insert` logic using a recursive helper method.
# - Enforced the core BST property: smaller values go left, larger values go right.


# Step 3
# Explanation: Let's add the `search` method. Searching in a BST is very efficient 
# because at each node, we can eliminate half of the remaining tree! We will use 
# another public method and a private recursive helper `_search` to traverse down 
# the correct path until we either find the value or hit a dead end (None).

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
            
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
                
    def search(self, value):
        # Kick off the recursive search starting from the root
        return self._search(value, self.root)
        
    def _search(self, value, current_node):
        # Base case 1: We hit a dead end, the value is not in the tree
        if current_node is None:
            return False
            
        # Base case 2: We found the value!
        if current_node.value == value:
            return True
            
        # Recursive cases: decide whether to search left or right
        if value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)

# What we accomplished in this step:
# - Implemented the `search` method to check if a value exists.
# - Wrote the recursive `_search` helper that leverages the BST property for fast lookups.


# Step 4
# Explanation: Finally, we want to view the contents of our tree. We will implement 
# an `in_order_traversal`. In a BST, an in-order traversal (visiting the Left child, 
# then the Node itself, then the Right child) naturally results in processing the 
# values in perfectly sorted order!

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
            
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
                
    def search(self, value):
        return self._search(value, self.root)
        
    def _search(self, value, current_node):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)
            
    def in_order_traversal(self):
        # We will collect the values in a list to easily print them
        elements = []
        self._in_order(self.root, elements)
        print("In-order traversal:", elements)
        return elements
        
    def _in_order(self, current_node, elements):
        if current_node is not None:
            # 1. Traverse the left subtree
            self._in_order(current_node.left, elements)
            # 2. Visit the node itself
            elements.append(current_node.value)
            # 3. Traverse the right subtree
            self._in_order(current_node.right, elements)

# What we accomplished in this step:
# - Implemented `in_order_traversal` to collect tree values.
# - Used a recursive helper to visit nodes in Left-Root-Right order.
# - Revealed the beautiful property that in-order traversal of a BST yields sorted data.


# Step 5
# Explanation: Our Binary Search Tree is now complete! Let's write a final script 
# to consolidate everything and run a test. We'll build a tree, insert a sequence of 
# numbers out of order, verify that our search works, and finally show that the 
# traversal prints them sorted.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
            
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
                
    def search(self, value):
        return self._search(value, self.root)
        
    def _search(self, value, current_node):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)
            
    def in_order_traversal(self):
        elements = []
        self._in_order(self.root, elements)
        print("In-order traversal:", elements)
        return elements
        
    def _in_order(self, current_node, elements):
        if current_node is not None:
            self._in_order(current_node.left, elements)
            elements.append(current_node.value)
            self._in_order(current_node.right, elements)


# Test our BST:
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    print("1. Inserting values: 50, 30, 70, 20, 40, 60, 80")
    # This structure naturally forms a balanced tree:
    #         50
    #       /    \
    #     30      70
    #    /  \    /  \
    #  20   40  60   80
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    
    print("\n2. Searching for existing value 40:")
    print("Found 40?", bst.search(40))
    # Expected output: Found 40? True
    
    print("\n3. Searching for non-existing value 99:")
    print("Found 99?", bst.search(99))
    # Expected output: Found 99? False
    
    print("\n4. Performing in-order traversal to see sorted values:")
    bst.in_order_traversal()
    # Expected output: In-order traversal: [20, 30, 40, 50, 60, 70, 80]


# CONGRATULATIONS! 🎉
# You've successfully built one of the most important data structures in computer science!
# 
# Key takeaways:
# - Binary Search Tree Property: You learned how keeping smaller values to the left and larger values to the right enables incredibly fast operations.
# - Recursion: You saw how naturally recursion fits with tree structures. Calling a method on the `left` or `right` node makes complex traversal simple.
# - Traversal Orders: You experienced how an in-order traversal inherently sorts the data by navigating the tree sequentially.
# - Searching Efficiency: For a balanced tree, finding a value discards half the remaining possibilities at each step (O(log N) complexity).
#
# Remember: The best way to learn is by doing! 🚀
