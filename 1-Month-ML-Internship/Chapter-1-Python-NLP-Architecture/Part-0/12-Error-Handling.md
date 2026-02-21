# 12: Error Handling - Try-Except

**Duration:** 40 minutes | **Difficulty:** Intermediate | **Key Skill:** Robust code with error handling

---

## í¾¯ What You'll Learn

- Try-except blocks
- Common exceptions
- Finally and else clauses
- Raising exceptions

---

## í³š Try-Except

\`\`\`python
try:
    result = 10 / 0  # Will raise error
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    value = int("hello")
except ValueError:
    print("Not a valid number")
\`\`\`

## í³š Multiple Except

\`\`\`python
try:
    value = int(input())
except ValueError:
    print("Enter a number")
except KeyboardInterrupt:
    print("User cancelled")
\`\`\`

---

## í·  ML Context

\`\`\`python
# Validate data
try:
    assert 0 <= probability <= 1
except AssertionError:
    print("Invalid probability")
\`\`\`

---
