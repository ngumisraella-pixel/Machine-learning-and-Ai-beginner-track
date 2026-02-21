# Control Flow (if/else, loops) - Summary Sheet

## Conditionals
\`\`\`python
if condition:
    # do this
elif other_condition:
    # do that
else:
    # fallback

# Comparison: ==, !=, <, >, <=, >=
# Logic: and, or, not
\`\`\`

## For Loops (Know count)
\`\`\`python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for item in lst:
    print(item)

for i, item in enumerate(lst):
    print(i, item)  # With index
\`\`\`

## While Loops (Unknown count)
\`\`\`python
i = 0
while i < 5:
    print(i)
    i += 1

while True:
    if condition:
        break  # Exit loop
    if skip_condition:
        continue  # Skip to next
\`\`\`

---
