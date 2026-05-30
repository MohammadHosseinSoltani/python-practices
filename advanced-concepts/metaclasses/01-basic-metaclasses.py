"""Question: Create a metaclass that automatically adds a 'created_at' timestamp attribute to any class that uses it. Demonstrate the metaclass by creating a simple class that prints its creation time."""

# LEARNING CHALLENGE
# Before looking at any solution below, please try to solve this yourself first!
# 
# Tips for success:
# - Understand that while an object is an instance of a class, a class is an instance of a metaclass!
# - A metaclass is created by inheriting from the built-in `type`.
# - You can intercept and modify class creation by overriding the `__new__` method in your metaclass.
# - Apply your metaclass to a regular class using the `metaclass=YourMetaclassName` syntax in the class definition.
# 
# Remember: The best way to learn programming is by doing, not by reading solutions!
# Take your time, experiment, and enjoy the learning process!






























# HINT SECTION
# - Define a class that inherits from `type` – that's your metaclass.
# - Override the `__new__` method in the metaclass to modify the class before it is created.
# - Use `import datetime` to generate the timestamp.
# - Set the `metaclass` keyword argument in the class definition (e.g., `class MyClass(metaclass=MyMetaclass):`).
# - Start simple and build up complexity gradually.

# ===============================================================================

# STEP-BY-STEP SOLUTION
# CLASSROOM-STYLE WALKTHROUGH

# Step 1
# Explanation: Let's start by looking at how we would normally solve this problem without 
# metaclasses. If we want every instance of a class to know when it was created, we manually 
# add a `created_at` attribute in the `__init__` method. This works, but if we had 50 different 
# classes that needed this, we would have to copy-paste this code 50 times.

import datetime

class NormalClass:
    def __init__(self):
        self.created_at = datetime.datetime.now()

# Test our normal class
obj = NormalClass()
print(f"Normal object created at: {obj.created_at}")

# What we accomplished in this step:
# - Implemented the desired behavior manually.
# - Identified the problem: this approach violates the DRY (Don't Repeat Yourself) principle 
#   if applied across many classes.


# Step 2
# Explanation: To solve this at a higher level, we introduce a metaclass. A metaclass is 
# simply a class that creates other classes. We do this by inheriting from `type`. 
# We override the `__new__` method, which is called *before* the class is actually created. 
# For now, we will just print a message to prove we have intercepted the class creation process.

import datetime

class TimestampMeta(type):
    # __new__ takes the metaclass itself, the class name, its base classes, and its attributes dict
    def __new__(mcs, name, bases, attrs):
        print(f"Intercepting creation of class: {name}")
        # We must call the parent 'type' to actually create the class
        return super().__new__(mcs, name, bases, attrs)

class TestClass(metaclass=TimestampMeta):
    pass

# Notice we don't even need to instantiate TestClass. 
# The print statement runs the moment the file is executed and the class is defined!

# What we accomplished in this step:
# - Created our first metaclass by inheriting from `type`.
# - Overrode `__new__` to hook into the class creation process.
# - Applied the metaclass using the `metaclass=` syntax.


# Step 3
# Explanation: Now let's modify the class while it is being created. In our metaclass, 
# we can inject new data directly into the `attrs` dictionary before we pass it to `super().__new__`. 
# Let's add a `class_created_at` timestamp. This will attach the timestamp to the *Class itself*, 
# not the instances.

import datetime

class TimestampMeta(type):
    def __new__(mcs, name, bases, attrs):
        # Injecting a new attribute into the class definition
        attrs['class_created_at'] = datetime.datetime.now()
        
        return super().__new__(mcs, name, bases, attrs)

class TestClass(metaclass=TimestampMeta):
    pass

# We access the attribute directly on the class, not an instance.
print(f"TestClass was defined at: {TestClass.class_created_at}")

# What we accomplished in this step:
# - Modified the `attrs` dictionary to dynamically add properties to a class.
# - Proved that metaclasses can alter a class's blueprint before it even exists in memory.


# Step 4
# Explanation: Adding an attribute to the class is cool, but our original goal was to add 
# a timestamp to every *instance* created from the class, without writing an `__init__` method 
# in the class itself. To do this, our metaclass must provide a custom `__init__` function 
# and inject it into the class's `attrs`. 
# Note: We check if the class already has an `__init__` so we don't accidentally delete it!

import datetime

class TimestampMeta(type):
    def __new__(mcs, name, bases, attrs):
        
        # Save the original __init__ if it exists
        original_init = attrs.get('__init__')

        # Define a new __init__ that adds our timestamp, then calls the original
        def new_init(self, *args, **kwargs):
            self.created_at = datetime.datetime.now()
            if original_init:
                original_init(self, *args, **kwargs)

        # Replace the class's __init__ with our wrapped version
        attrs['__init__'] = new_init
        
        return super().__new__(mcs, name, bases, attrs)

class User(metaclass=TimestampMeta):
    def __init__(self, username):
        self.username = username

user = User("Alice")
print(f"User {user.username} created at: {user.created_at}")

# What we accomplished in this step:
# - Used a metaclass to inject dynamic behavior into a class's instantiation process.
# - Carefully wrapped existing methods so we didn't break the original class design.


# Step 5
# Explanation: For our final step, let's consolidate everything into a clean demonstration. 
# We will define our robust metaclass, create a couple of different classes that use it, 
# and instantiate them with a small delay to prove that the timestamps are unique for each instance.

import datetime
import time

class TimestampMeta(type):
    """A metaclass that automatically injects a 'created_at' attribute into all instances."""
    def __new__(mcs, name, bases, attrs):
        original_init = attrs.get('__init__')

        def new_init(self, *args, **kwargs):
            self.created_at = datetime.datetime.now()
            if original_init:
                original_init(self, *args, **kwargs)

        attrs['__init__'] = new_init
        return super().__new__(mcs, name, bases, attrs)

# Test our code:
class Document(metaclass=TimestampMeta):
    def __init__(self, title):
        self.title = title

class Message(metaclass=TimestampMeta):
    def __init__(self, content):
        self.content = content

print("--- Metaclass Demonstration ---")

doc = Document("Python Metaclasses Guide")
print(f"Document '{doc.title}' instantiated at: {doc.created_at}")
# Expected output: Document 'Python Metaclasses Guide' instantiated at: 2023-10-25 14:32:01.123456

time.sleep(1) # Wait 1 second to see the timestamp change

msg = Message("Hello, world!")
print(f"Message '{msg.content}' instantiated at: {msg.created_at}")
# Expected output: Message 'Hello, world!' instantiated at: 2023-10-25 14:32:02.124567

# What we accomplished in this step:
# - Created a fully functional, reusable metaclass.
# - Applied the metaclass to entirely different classes.
# - Demonstrated that our injected `__init__` logic works perfectly on a per-instance basis.


# CONGRATULATIONS! 🎉
# You have successfully ventured into the deepest magic of Python: Metaclasses!
# 
# Key takeaways:
# - If objects are instances of classes, classes are instances of metaclasses.
# - You create a metaclass by inheriting from the built-in `type`.
# - The `__new__` method in a metaclass allows you to intercept and modify the class dictionary (`attrs`) 
#   before the class is formally created in memory.
# - Metaclasses are powerful tools for building frameworks (like Django or SQLAlchemy) because they 
#   allow you to enforce rules or automatically add behaviors to user-defined classes seamlessly.
# 
# Keep experimenting! Try modifying the metaclass so that it forces all method names in the class 
# to be lowercase, raising an error during class definition if a developer uses CamelCase!
# 
# Remember: The best way to learn is by doing! 🚀
