# Functions Examples

# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!

# Function with defaults
def add(a, b=10):
    return a + b

print(add(5))      # 15 (uses default)
print(add(5, 3))   # 8 (overrides default)

# Multiple return values
def get_user_info():
    return "Alice", 30, "NYC"

name, age, city = get_user_info()
print(name, age, city)

# Function with list parameter
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list([1, 2, 3, 4, 5]))  # 15

# Variable arguments
def print_all(*args):
    for item in args:
        print(item)

print_all("a", "b", "c")

# Keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
