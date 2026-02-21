# Advanced Concepts Quizzes

## File I/O Quiz
1. Write syntax to open "data.txt" for reading
2. What does `with` do when opening files?
3. Read entire file to string or lines?
4. How to write text to file?

**Answers:** 1. `open("data.txt", "r")` 2. Auto-closes file 3. `.read()` vs `.readlines()` 4. `.write(text)`

## Error Handling Quiz
1. What keyword tries risky code?
2. What keyword catches errors?
3. Can you catch multiple exceptions?
4. What's the finally block for?

**Answers:** 1. `try` 2. `except` 3. Yes 4. Cleanup code

## Comprehensions Quiz
1. List comprehension syntax?
2. Can you filter in comprehension?
3. Nested list comp for 2D list?
4. How are they faster?

**Answers:** 1. `[x for x in range(10)]` 2. `[x for x in lst if x > 5]` 3. `[[x*y for x in a] for y in b]` 4. Optimized internally

## Lambda Quiz
1. Lambda returns: single/multiple values?
2. Use case vs regular function?
3. Common with map()?
4. Sort with lambda?

**Answers:** 1. Single value 2. Small, one-off functions 3. Yes 4. `sort(key=lambda x: ...)`

---
