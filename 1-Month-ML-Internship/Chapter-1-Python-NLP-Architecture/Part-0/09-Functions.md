# 09: Functions - Reusable Code

**Duration:** 60 minutes | **Difficulty:** Beginner-Intermediate | **Key Skill:** Code organization

---

## í¾¯ What You'll Learn

- Defining functions
- Parameters and arguments
- Return values
- Default parameters
- *args and **kwargs

---

## í³š Core Concept: Functions

A function is a reusable block of code that performs a specific task.

### Basic Function

\`\`\`python
def greet():
    print("Hello!")

greet()  # Call function
\`\`\`

### Parameters & Arguments

\`\`\`python
def add(a, b):
    result = a + b
    return result

sum_val = add(5, 3)  # 8
\`\`\`

### Default Parameters

\`\`\`python
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (uses default exponent=2)
print(power(5, 3))   # 125 (exponent=3)
\`\`\`

---

## í·  ML Context

### Preprocessing Function

\`\`\`python
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)

# Use in preprocessing
score = 75
normalized = normalize(score, 0, 100)
\`\`\`

---

## í´‘ Key Takeaways

âœ… Functions make code reusable
âœ… Use parameters to pass data in
âœ… Use return to send data out
âœ… Default parameters provide flexibility
âœ… Functions are fundamental to organization

---
