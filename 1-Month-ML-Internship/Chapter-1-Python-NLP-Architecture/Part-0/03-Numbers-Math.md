# 03: Numbers & Mathematical Operations

**Duration:** 40 minutes | **Difficulty:** Beginner-Intermediate | **Key Skill:** Numerical computations for ML

---

## í¾¯ What You'll Learn

- Arithmetic operations (+ - * / // % **)
- Mathematical functions
- Operator precedence
- Working with the math module
- ML Context: Foundation for all numerical algorithms

---

## í³š Core Concept: Arithmetic Operations

Python treats numbers naturally. All arithmetic operations follow standard mathematical rules with some Python-specific quirks you need to know.

### Basic Arithmetic Operations

\`\`\`python
# Addition
a = 10
b = 3
sum_result = a + b       # 13

# Subtraction
difference = a - b       # 7

# Multiplication
product = a * b          # 30

# Division (always returns float!)
division = a / b         # 3.3333... (float)

# Integer Division (floor division - rounds down)
int_division = a // b    # 3 (removes decimal)

# Modulo (remainder after division)
remainder = a % b        # 1 (because 10 = 3*3 + 1)

# Exponentiation (power)
power = a ** b           # 1000 (10 to the power of 3)
square = 5 ** 2          # 25

# Combining operations
result = 2 + 3 * 4       # 14 (multiplication first due to precedence)
\`\`\`

### Important: Division Returns Float

\`\`\`python
# Key difference for beginners
print(10 / 2)            # 5.0 (FLOAT, not int!)
print(10 // 2)           # 5 (INT - integer division)
print(type(10 / 2))      # <class 'float'>
print(type(10 // 2))     # <class 'int'>
\`\`\`

## í´‘ Key Takeaways

âœ… Division (/) always returns float; use // for integer division
âœ… The math module provides functions for scientific computing
âœ… Follow operator precedence rules (use parentheses when unsure)
âœ… Float precision can cause small rounding errors
âœ… Compound operators (+=, -=, etc.) are shortcuts
âœ… These operations are foundations for ML algorithms

---

## íº€ Next: [04-Lists](./04-Lists.md)

Lists are the most important data structure in Python. Learn to master them!
