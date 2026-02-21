# Advanced Concepts Examples

# List Comprehension
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtering with comprehension
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Lambda functions
double = lambda x: x * 2
print(double(5))  # 10

# Map with lambda
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Filter with lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# Sorting with lambda
students = [("Alice", 90), ("Bob", 75), ("Charlie", 85)]
sorted_by_grade = sorted(students, key=lambda x: x[1])
print(sorted_by_grade)

# Error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Cleanup code here")
