# Tips & Tricks - Part 0

## 1. Useful Built-in Functions

\`\`\`python
# zip() - Combine lists
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# enumerate() - Get index and value
for i, item in enumerate(["a", "b", "c"]):
    print(i, item)

# sum(), min(), max()
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
biggest = max(numbers)
smallest = min(numbers)

# sorted() - Create sorted list
names = ["Charlie", "Alice", "Bob"]
sorted_names = sorted(names)
\`\`\`

## 2. List Tricks

\`\`\`python
# Copy a list (don't use =)
original = [1, 2, 3]
copy = original.copy()  # or original[:]

# Extend vs append
lst = [1, 2]
lst.append([3, 4])   # Adds list as single item: [1, 2, [3, 4]]
lst2 = [1, 2]
lst2.extend([3, 4])  # Adds items: [1, 2, 3, 4]

# Multiple assignment
a, b, c = [1, 2, 3]
\`\`\`

## 3. String Tricks

\`\`\`python
# Multiply strings
"ab" * 3  # "ababab"

# Join is faster than concatenation
", ".join(["a", "b", "c"])  # "a, b, c"

# Split with limit
"a:b:c".split(":", 1)  # ["a", "b:c"]
\`\`\`

## 4. Dictionary Tricks

\`\`\`python
# Get with default
d = {"a": 1}
d.get("b", 0)  # 0 (default)

# Check membership
"a" in d  # True

# Unpack
d = {"x": 1, "y": 2}
{"x": x, "y": y} = d  # ❌ Wrong syntax
# Use: x, y = d.values()
\`\`\`

## 5. F-string Power

\`\`\`python
value = 42
print(f"Value: {value}")           # Simple

print(f"Value: {value:05d}")       # Pad with zeros
print(f"Value: {3.14159:.2f}")     # 2 decimal places
print(f"Value: {value:.2%}")       # As percentage
\`\`\`

---
