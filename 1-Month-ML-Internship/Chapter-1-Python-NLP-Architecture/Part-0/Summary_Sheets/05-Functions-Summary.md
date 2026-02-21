# Functions - Summary Sheet

## Define & Call
\`\`\`python
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")  # Call function
\`\`\`

## Parameters & Defaults
\`\`\`python
def add(a, b=10):      # b has default
    return a + b

add(5)      # Uses default: 5 + 10
add(5, 3)   # Overrides default: 5 + 3
\`\`\`

## Multiple Return Values
\`\`\`python
def divide(a, b):
    return a, b // a  # Return tuple
    
q, r = divide(10, 3)  # Unpack results
\`\`\`

## Key Points
- Define with `def`, call with ()
- Parameters are inputs, return is output
- Return None if no return statement
- *args for variable arguments
- **kwargs for keyword arguments

---
