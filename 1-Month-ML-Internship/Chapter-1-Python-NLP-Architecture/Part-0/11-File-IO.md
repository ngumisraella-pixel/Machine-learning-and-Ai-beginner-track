# 11: File I/O - Reading & Writing Files

**Duration:** 45 minutes | **Difficulty:** Intermediate | **Key Skill:** Working with files

---

## í¾¯ What You'll Learn

- Reading files
- Writing files
- Working with file paths
- CSV and JSON basics

---

## í³š Reading Files

\`\`\`python
# Read entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
\`\`\`

## í³š Writing Files

\`\`\`python
# Write to file
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# Append to file
with open("output.txt", "a") as file:
    file.write("\nNew line")
\`\`\`

---

## í·  ML Context

\`\`\`python
# Save predictions
with open("predictions.txt", "w") as f:
    for pred in predictions:
        f.write(f"{pred}\n")
\`\`\`

---
