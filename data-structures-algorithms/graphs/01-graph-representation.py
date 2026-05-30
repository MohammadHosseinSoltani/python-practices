"""Question: Implement a Graph class using an adjacency list. It should support adding vertices, adding edges (for an undirected graph), and performing a Breadth-First Search (BFS) starting from a given vertex."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Think about using a Python dictionary to store your vertices, where each vertex maps to a list of its neighboring vertices (the adjacency list).
# - For the Breadth-First Search (BFS), you will need a queue to keep track of which vertex to visit next, and a set to remember which ones you have already visited.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Use a dictionary `self.graph` where keys are vertex names and values are lists of neighboring vertex names.
# - For `add_vertex`, add a new key with an empty list if it doesn't already exist.
# - For `add_edge`, append each vertex to the other's neighbor list to make it undirected.
# - For BFS, use `collections.deque` as a queue. Start from the given vertex, mark it as visited, and repeatedly dequeue a vertex and enqueue its unvisited neighbors.
# - Print vertices in the order they are visited.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by defining our Graph class. There are many ways to represent 
# a graph in code, but the most common and versatile is the "adjacency list". In Python, 
# a dictionary is perfect for this! The keys will be the vertex (node) names, and the 
# values will be lists of their neighboring vertices. We will also write a simple 
# `add_vertex` method to safely insert new, disconnected vertices into our graph.

class Graph:
    def __init__(self):
        # Our adjacency list representation
        self.graph = {}
        
    def add_vertex(self, vertex):
        # Only add the vertex if it is not already in the graph
        if vertex not in self.graph:
            self.graph[vertex] = []

# What we accomplished in this step:
# - Created the `Graph` class structure.
# - Initialized an empty dictionary to serve as our adjacency list.
# - Implemented `add_vertex` to add isolated nodes safely without overwriting existing ones.


# Step 2
# Explanation: Now we'll add the ability to connect our vertices using the `add_edge` method. 
# Because we are building an undirected graph, an edge from A to B means there is also 
# an edge from B to A. We will first ensure both vertices exist in our dictionary 
# (using our `add_vertex` method), and then append each vertex to the other's list of neighbors.

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            
    def add_edge(self, vertex1, vertex2):
        # Ensure both vertices exist in the graph before connecting them
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        # Since this is an undirected graph, we add the connection in both directions
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

# What we accomplished in this step:
# - Implemented `add_edge` to create connections between vertices.
# - Handled the bidirectional nature of undirected graphs.
# - Ensured that adding an edge automatically adds any missing vertices.


# Step 3
# Explanation: To see what we are building, we need a way to display the graph. We will 
# add a `display` method that iterates through our dictionary and prints each vertex 
# alongside its neighbors. We will also do a quick test in our minds (or code) to ensure 
# our edges are forming correctly.

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
        
    def display(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {neighbors}")

# What we accomplished in this step:
# - Added a `display` method to easily visualize our adjacency list structure.
# - Prepared our class for testing complex networks.


# Step 4
# Explanation: Now for the fun part: traversing the graph using Breadth-First Search (BFS)! 
# BFS explores the graph outward in "layers" or "levels". It visits a starting vertex, 
# then all of its immediate neighbors, then all of their neighbors, and so on. To do this, 
# we use a queue (first-in, first-out) to track what to visit next, and a `visited` set 
# to ensure we don't get trapped in endless cycles (which are very common in graphs!).

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
        
    def display(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {neighbors}")
            
    def bfs(self, start_vertex):
        # Safety check: if the start vertex isn't in the graph, we can't search
        if start_vertex not in self.graph:
            return []
            
        visited = set()
        queue = deque([start_vertex])
        # Mark the start vertex as visited immediately before entering the loop
        visited.add(start_vertex)
        
        bfs_order = []
        
        while queue:
            # Dequeue the next vertex to process
            current_vertex = queue.popleft()
            bfs_order.append(current_vertex)
            
            # Look at all its neighboring vertices
            for neighbor in self.graph[current_vertex]:
                # If we haven't visited this neighbor yet, queue it up!
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return bfs_order

# What we accomplished in this step:
# - Implemented the `bfs` method for layer-by-layer traversal.
# - Utilized a `collections.deque` for efficient, O(1) queue operations.
# - Used a `set` to track visited nodes and perfectly prevent infinite loops.


# Step 5
# Explanation: Our Graph class is beautifully complete! Let's put everything into our 
# final script. We will build a small, interconnected graph (like a mini social network 
# or a map of cities), display its internal dictionary, and finally perform a BFS to 
# observe the exact order the algorithm explores the nodes.

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
        
    def display(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {neighbors}")
            
    def bfs(self, start_vertex):
        if start_vertex not in self.graph:
            return []
            
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        
        bfs_order = []
        
        while queue:
            current_vertex = queue.popleft()
            bfs_order.append(current_vertex)
            
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return bfs_order


# Test our graph:
if __name__ == "__main__":
    my_graph = Graph()
    
    print("1. Building the graph...")
    # Let's imagine a network mapped out like this:
    #    A --- B
    #    |     | \
    #    C --- D - E
    my_graph.add_edge("A", "B")
    my_graph.add_edge("A", "C")
    my_graph.add_edge("B", "D")
    my_graph.add_edge("B", "E")
    my_graph.add_edge("C", "D")
    my_graph.add_edge("D", "E")
    
    print("\n2. Graph Adjacency List (Internal Representation):")
    my_graph.display()
    # Expected output (order of neighbors might vary slightly depending on insertion):
    # A -> ['B', 'C']
    # B -> ['A', 'D', 'E']
    # C -> ['A', 'D']
    # D -> ['B', 'C', 'E']
    # E -> ['B', 'D']
    
    print("\n3. Performing Breadth-First Search starting from vertex 'A':")
    traversal = my_graph.bfs("A")
    print("BFS Traversal Order:", traversal)
    # Expected output (depending on list order, C and B might swap, but A is first, 
    # and E is typically last):
    # BFS Traversal Order: ['A', 'B', 'C', 'D', 'E']


# CONGRATULATIONS! 🎉
# You have successfully built a Graph data structure and navigated it using BFS!
#
# Key takeaways:
# - Adjacency List Representation: You learned how dictionaries make an incredibly efficient and intuitive way to map out nodes and their connections in Python.
# - Undirected Edges: By adding each vertex to the other's neighbor list, you created a two-way street between them.
# - Queue Usage: You saw how a First-In-First-Out (FIFO) queue perfectly enables level-by-level exploration.
# - BFS Traversal Order: You experienced how BFS finds the shortest path (in terms of the number of edges) from the start vertex to any other reachable vertex.
#
# Remember: The best way to learn is by doing! 🚀
