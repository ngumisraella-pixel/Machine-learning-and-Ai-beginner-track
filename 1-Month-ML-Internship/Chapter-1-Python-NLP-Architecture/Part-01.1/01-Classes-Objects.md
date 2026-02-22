# 01: Classes & Objects - Creating Custom Types

**Duration:** 60 minutes | **Difficulty:** Intermediate | **Key Skill:** OOP fundamentals

---

## í¾¯ What You'll Learn

- Defining classes and creating objects
- Attributes and methods
- The `__init__` constructor
- Self parameter and instance variables
- ML Context: Building model classes

---

## í³š Core Concept: Classes

A **class** is a blueprint for creating objects with shared attributes and methods.

### Basic Class Structure

\`\`\`python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"

# Create objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())  # Buddy says Woof!
\`\`\`

### Attributes & Methods

\`\`\`python
class Student:
    school = "ML Academy"  # Class attribute
    
    def __init__(self, name, gpa):
        self.name = name      # Instance attribute
        self.gpa = gpa
    
    def study(self, hours):
        return f"{self.name} studied for {hours} hours"
\`\`\`

---

## í·  ML Context: Model Classes

\`\`\`python
class SimpleModel:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
        self.weights = None
    
    def train(self, X, y):
        # Training logic
        pass
    
    def predict(self, X):
        # Prediction logic
        pass
\`\`\`

---

## í´‘ Key Takeaways

âœ… Classes organize code into reusable templates
âœ… Objects are instances of classes
âœ… __init__ initializes instance attributes
âœ… Methods are functions inside classes
âœ… self refers to the current object

---
