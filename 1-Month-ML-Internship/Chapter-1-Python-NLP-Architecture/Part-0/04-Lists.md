# 04: Lists - Python's Most Important Data Structure

**Duration:** 60 minutes | **Difficulty:** Beginner | **Key Skill:** List operations and manipulation

---

## í¾¯ What You'll Learn

- Creating and accessing lists
- List methods (append, insert, remove, pop, sort, etc.)
- List slicing and iteration
- The enumerate() function
- ML Context: Lists hold datasets, features, and predictions

---

## í³š Core Concept: Lists

A **list** is an ordered collection of items. Unlike strings, lists are mutable (changeable), making them perfect for data manipulation in ML.

### Creating Lists

\`\`\`python
# Empty list
empty_list = []

# List with integers
ages = [25, 30, 35, 28]

# List with mixed types
mixed = [42, "Alice", 3.14, True]

# List with strings
fruits = ["apple", "banana", "orange"]

# Using list() constructor
numbers = list(range(5))  # [0, 1, 2, 3, 4]
\`\`\`

### Accessing Elements

\`\`\`python
fruits = ["apple", "banana", "orange", "grape"]

# Indexing (positions start at 0)
print(fruits[0])     # "apple"
print(fruits[1])     # "banana"
print(fruits[-1])    # "grape" (last item)
print(fruits[-2])    # "orange" (second from end)

# Length
print(len(fruits))   # 4
\`\`\`

### List Slicing

\`\`\`python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])    # [2, 3, 4]
print(numbers[:3])     # [0, 1, 2]
print(numbers[5:])     # [5, 6, 7, 8, 9]
print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd)
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed!)
\`\`\`

## âœï¸ Modifying Lists

### Adding Elements

\`\`\`python
fruits = ["apple", "banana"]

# Append (add to end)
fruits.append("orange")  # ["apple", "banana", "orange"]

# Insert (at specific position)
fruits.insert(1, "grape")  # ["apple", "grape", "banana", "orange"]

# Extend (add multiple items)
fruits.extend(["mango", "pear"])  # Add list to list
\`\`\`

### Removing Elements

\`\`\`python
fruits = ["apple", "banana", "orange", "grape"]

# Remove by value
fruits.remove("banana")  # ["apple", "orange", "grape"]

# Pop (remove and return last item)
last = fruits.pop()  # "grape", list is now ["apple", "orange"]

# Pop at index
first = fruits.pop(0)  # "apple", list is now ["orange"]

# Clear all
fruits.clear()  # []
\`\`\`

---

## í´ Essential List Methods

\`\`\`python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Sort (in place)
numbers.sort()  # [1, 1, 2, 3, 4, 5, 6, 9]

# Count occurrences
count = numbers.count(1)  # 2

# Find index
index = numbers.index(4)  # 2

# Copy list (important!)
copy = numbers.copy()  # New list with same values
\`\`\`

---

## í´„ Iterating Through Lists

\`\`\`python
fruits = ["apple", "banana", "orange"]

# Simple loop
for fruit in fruits:
    print(fruit)

# With index using enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    # Output:
    # 0: apple
    # 1: banana
    # 2: orange

# Using range and len() (less common)
for i in range(len(fruits)):
    print(fruits[i])
\`\`\`

---

## í·  ML Context: Lists for ML

### Dataset Representation

\`\`\`python
# Features (X) - input data
features = [
    [2.5, 3.1],   # Sample 1: [age, score]
    [3.2, 2.8],   # Sample 2
    [1.8, 4.2],   # Sample 3
]

# Labels (y) - output/target
labels = ["cat", "dog", "cat"]

# Predictions from model
predictions = [0.92, 0.15, 0.88]
\`\`\`

### Feature Normalization

\`\`\`python
# Raw dataset
data = [100, 50, 75, 25]

# Min-max normalization
min_val = min(data)
max_val = max(data)
normalized = [(x - min_val) / (max_val - min_val) for x in data]
\`\`\`

---

## í³ Exercises  

### Try It! (Quick Checks)

**Exercise 4.1: Basic Lists**
\`\`\`python
numbers = [10, 20, 30, 40, 50]

# 1. Print first element
# 2. Print last element  
# 3. Print length
# 4. Print elements from index 1 to 3
\`\`\`

**Exercise 4.2: Modifying Lists**
\`\`\`python
grades = [85, 90, 78]

# 1. Add 92 to the list
# 2. Insert 88 at position 1
# 3. Remove 78
# 4. Print the result
\`\`\`

### Do It! (Hands-on Practice)

**Exercise 4.3: Word Frequency Counter**
\`\`\`python
words = ["the", "quick", "brown", "fox", "the", "lazy", "fox"]

# 1. Count occurrences of "the"
# 2. Count occurrences of "fox"
# 3. Find index of first "brown"
# 4. Create list of unique words
\`\`\`

**Exercise 4.4: Data Normalization**
\`\`\`python
# Normalize test scores to 0-1 range
scores = [55, 65, 75, 85, 95]

min_score = min(scores)
max_score = max(scores)

# Normalize: (score - min) / (max - min)
# Create normalized_scores list
\`\`\`

### Master It! (Challenges)

**Exercise 4.5: Grade Statistics**
\`\`\`python
grades = [85, 92, 78, 95, 88, 76, 91]

# Calculate:
# 1. Average grade
# 2. Highest grade
# 3. Lowest grade
# 4. Count of grades >= 90
# 5. Print as formatted report
\`\`\`

---

## í´‘ Key Takeaways

âœ… Lists are ordered, changeable collections
âœ… Index from 0; use negative indices for last items
âœ… Slice with [start:end:step]
âœ… Use append(), insert(), remove(), pop() to modify
âœ… Iterate with for loops or enumerate()
âœ… Lists are fundamental for ML data representations

---

## íº€ Next: [05-Dictionaries](./05-Dictionaries.md)

Dictionaries store key-value pairs - perfect for labeled data!
