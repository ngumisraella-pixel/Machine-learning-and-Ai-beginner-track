# Collections (Lists, Dicts, Tuples) - Summary Sheet

## Lists (Mutable, Ordered)
\`\`\`python
lst = [1, 2, 3]
lst.append(4)      # Add to end
lst.pop()          # Remove last
lst[0] = 99        # Change item
for x in lst: ...  # Iterate
\`\`\`

## Dictionaries (Key-Value, Mutable)
\`\`\`python
d = {"name": "Alice", "age": 30}
d["name"]          # Access value
d.keys()           # Get all keys
d.values()         # Get all values
d.items()          # Get key-value pairs
d.get("age")       # Safe access
\`\`\`

## Tuples (Immutable, Ordered)
\`\`\`python
t = (1, 2, 3)
t[0]               # Access (no change)
x, y, z = t        # Unpack
for item in t: ... # Iterate
\`\`\`

## Sets (Unique, Unordered)
\`\`\`python
s = {1, 2, 3}
s.add(4)           # Add item
s.remove(1)        # Remove item
s1 & s2            # Intersection
s1 | s2            # Union
\`\`\`

---
