# Common Code Patterns in Part 0

## Pattern 1: Accumulator

\`\`\`python
# Count occurrences
count = 0
for item in data:
    if condition(item):
        count += 1

# Build a sum
total = 0
for num in numbers:
    total += num
# Or: total = sum(numbers)
\`\`\`

## Pattern 2: Filtering

\`\`\`python
# Remove unwanted items
filtered = [x for x in data if x > threshold]

# Using filter()
filtered = list(filter(lambda x: x > threshold, data))
\`\`\`

## Pattern 3: Transformation

\`\`\`python
# Apply function to each item
doubled = [x * 2 for x in numbers]

# Using map()
doubled = list(map(lambda x: x * 2, numbers))
\`\`\`

## Pattern 4: Pairing

\`\`\`python
# Pair keys with values
for key, value in data_dict.items():
    print(f"{key}: {value}")

# Pair from two lists
for item1, item2 in zip(list1, list2):
    print(item1, item2)
\`\`\`

## Pattern 5: Nested Loop

\`\`\`python
# Process all combinations
for item1 in list1:
    for item2 in list2:
        process(item1, item2)

# Using list comprehension
results = [(x, y) for x in list1 for y in list2]
\`\`\`

---
