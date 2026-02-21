# 11: File I/O - Reading & Writing Files

**Duration:** 50 minutes | **Difficulty:** Beginner | **Key Skill:** Data persistence

---

## í¾¯ What You'll Learn

- Reading files
- Writing files
- Appending to files
- Closing files with context managers

---

## í³š Reading Files

\`\`\`python
# Open and read
with open("data.txt", "r") as file:
    content = file.read()

# Read line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
\`\`\`

### Writing Files

\`\`\`python
# Write (overwrites)
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# Append (adds to end)
with open("output.txt", "a") as file:
    file.write("\nNew line")
\`\`\`

---

## í·  ML Context

\`\`\`python
# Read dataset
with open("dataset.csv", "r") as file:
    lines = file.readlines()

# Process and write results
with open("results.txt", "w") as file:
    for line in lines:
        processed = line.strip()
        file.write(processed + "\n")
\`\`\`

---

## í´‘ Key Takeaways

âœ… Use "with" for automatic file closing
âœ… "r" reads, "w" writes, "a" appends
âœ… File I/O is critical for datasets
âœ… Always close files to prevent data loss

---
