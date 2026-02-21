# File I/O Examples

# Writing to file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")

# Reading entire file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Readlines (as list)
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(f"First line: {lines[0]}")

# Appending to file
with open("example.txt", "a") as file:
    file.write("This is appended\n")
