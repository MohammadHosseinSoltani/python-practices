"""Question: Explore Python's module system internals. Inspect the search path for modules using `sys.path`, list all names defined in a module using `dir()`, and demonstrate how to reload a module after modifying it using `importlib.reload`."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Import `sys` and `importlib`.
# - Use `sys.path` to see the directories where Python looks for modules.
# - Use `dir()` on a module to list all the names (functions, classes, variables) defined inside it.
# - Use `importlib.reload(module)` to reload a module after it has been imported.
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Import `sys` and print `sys.path` to see the list of directories Python searches for modules.
# - Import a module (like the `math` module) and use `dir(math)` to see all functions and constants it contains.
# - Import `importlib` and use `importlib.reload(module)` to reload a module after you've made changes to it.
# - Try creating a simple module file, import it, list its contents with `dir()`, then modify the file and reload it to see the changes.
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by looking under the hood to see how Python finds modules. 
# When you type `import math`, how does Python know where to look? It checks a list of 
# directories stored in `sys.path`. We will import the built-in `sys` module and print 
# out this list to inspect the search path.

import sys

# We print the first few paths to keep the output clean.
# The first entry (index 0) is usually the directory of the script you are currently running.
print("Python's module search path (first 3 entries):")
for path in sys.path[:3]:
    print(f"- {path}")

# What we accomplished in this step:
# - We imported the `sys` module, which provides access to system-specific parameters.
# - We inspected `sys.path` to understand exactly where Python looks for imported files.


# Step 2
# Explanation: Now let's explore introspection, which is the ability of a program to 
# examine its own structure. We will import the built-in `math` module and use the 
# `dir()` function. `dir()` returns a list of all the names (variables, functions, 
# classes) defined inside that module.

import sys
import math

print("Python's module search path (first 3 entries):")
for path in sys.path[:3]:
    print(f"- {path}")

print("\nInspecting the 'math' module using dir():")
math_names = dir(math)

# The math module has many items; we will just print the first 10.
# Notice that many built-in attributes start and end with double underscores (dunder methods).
for name in math_names[:10]:
    print(f"- {name}")

# What we accomplished in this step:
# - We imported the `math` module.
# - We used the `dir()` function to look inside the module and discover what tools are available.


# Step 3
# Explanation: Let's see how `dir()` works on a custom module. We will pretend you have 
# created a file named `simple_module.py` in the same folder. We show its contents 
# as a comment below. We will try to import it safely and inspect it.

import sys
import math

# --- Contents of simple_module.py ---
# version = 1.0
# 
# def greet():
#     print("Hello from version 1!")
# ------------------------------------

print("Inspecting a custom module:")
try:
    import simple_module
    
    # Let's see what names exist inside our custom module
    module_contents = dir(simple_module)
    print(f"Names in simple_module: {module_contents}")
    
except ImportError:
    print("(Notice: 'simple_module.py' not found. Create it in this directory to see it in action!)")

# What we accomplished in this step:
# - We applied the `dir()` function to a custom module.
# - We learned that custom variables and functions (like 'version' and 'greet') will appear alongside Python's default dunder attributes.


# Step 4
# Explanation: A critical piece of module internals is caching. When Python imports a 
# module, it stores it in a dictionary called `sys.modules`. If you try to import it 
# again, Python just uses the cached version to save time. But what if you edit the 
# module file while the program is running? You need `importlib.reload` to force 
# Python to read the file again. We will simulate modifying the file and reloading it.

import sys
import math
import importlib

print("Demonstrating module reloading:")
try:
    import simple_module
    print("Initial import successful.")
    
    # Imagine we pause our program here, open simple_module.py, 
    # change version to 2.0, and save the file.
    
    # A standard import won't pick up the changes due to caching:
    import simple_module 
    
    # To force Python to read our updated file from the disk, we use reload:
    importlib.reload(simple_module)
    print("Module successfully reloaded from disk!")
    
except ImportError:
    print("(Notice: Create 'simple_module.py' to test the reload functionality.)")

# What we accomplished in this step:
# - We imported the `importlib` library.
# - We learned about module caching and how standard imports ignore subsequent calls.
# - We used `importlib.reload()` to force an update, which is incredibly useful during active development.


# Step 5
# Explanation: Let's consolidate our exploration into a clean, complete script. We will 
# wrap our logic into a function so we can clearly see the execution flow. We will add 
# print statements that act as our final test demonstration.

import sys
import math
import importlib

def explore_module_internals():
    print("--- 1. Inspecting Module Search Path ---")
    print(f"First entry in sys.path: {sys.path[0]}")
    print("This is where Python starts looking for modules (usually the current directory).\n")
    
    print("--- 2. Introspection with dir() ---")
    math_names = dir(math)
    print(f"The 'math' module contains {len(math_names)} items.")
    print(f"First 5 items: {math_names[:5]}\n")
    
    print("--- 3. Module Caching and Reloading ---")
    try:
        import simple_module
        
        # Check the current sys.modules cache
        is_cached = 'simple_module' in sys.modules
        print(f"Is simple_module cached in sys.modules? {is_cached}")
        
        print("Reloading simple_module...")
        reloaded_module = importlib.reload(simple_module)
        print("Reload complete!")
        
    except ImportError:
        print("Skipping reload demo. (Create 'simple_module.py' to test this!)")

# Test our code:
if __name__ == "__main__":
    explore_module_internals()
    
    # Expected Output Example (paths will vary based on your system):
    # --- 1. Inspecting Module Search Path ---
    # First entry in sys.path: /Users/learner/python-practices/fundamentals/modules
    # This is where Python starts looking for modules (usually the current directory).
    #
    # --- 2. Introspection with dir() ---
    # The 'math' module contains 65 items.
    # First 5 items: ['__doc__', '__file__', '__loader__', '__name__', '__package__']
    #
    # --- 3. Module Caching and Reloading ---
    # Skipping reload demo. (Create 'simple_module.py' to test this!)

# What we accomplished in this step:
# - We consolidated our exploration into a neat, reusable function.
# - We verified whether our module was present in `sys.modules` cache.
# - We created a complete reference script for Python module internals.

# ===============================================================================
# CONGRATULATIONS! 🎉
# You've achieved an expert-level understanding of how Python manages modules under the hood! 🛠️
# You learned that `sys.path` is just a list of directories that Python checks, you 
# used `dir()` to peek inside a module's namespace dynamically, and you discovered how 
# to bypass `sys.modules` caching using `importlib.reload()`. These are incredibly 
# powerful debugging and development tools that separate beginners from advanced Python developers.
# Remember: The best way to learn is by doing! 🚀
