# Debugging Strategies

## Strategy 1: Print Debugging

\`\`\`python
def my_function(data):
    print(f"Input data: {data}")
    print(f"Type: {type(data)}")
    
    result = process(data)
    print(f"After processing: {result}")
    
    return result
\`\`\`

## Strategy 2: Type Checking

\`\`\`python
def process(value):
    if not isinstance(value, int):
        print(f"ERROR: Expected int, got {type(value)}")
        return None
    return value * 2
\`\`\`

## Strategy 3: Assertion

\`\`\`python
def divide(a, b):
    assert b != 0, "Cannot divide by zero!"
    return a / b
\`\`\`

## Strategy 4: Step Through Mentally

1. What is the initial value?
2. What happens after each operation?
3. What is the final value?
4. Is it what we expect?

## Strategy 5: Reduce the Problem

\`\`\`python
# If this doesn't work:
result = process_big_data(huge_list)

# Test with simpler input:
result = process_big_data([1, 2, 3])

# Test function in isolation:
result = my_func(5)
\`\`\`

---
