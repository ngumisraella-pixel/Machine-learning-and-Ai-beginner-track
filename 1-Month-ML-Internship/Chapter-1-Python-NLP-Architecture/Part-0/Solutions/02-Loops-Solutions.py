# 02-Loops-Solutions.py - SOLUTIONS

# Solution 1: Sum Calculator
total = sum(range(1, 101))
print(f"Sum 1-100: {total}")

# Solution 2: Pass/Fail Indicator
scores = [45, 78, 92, 65, 88, 52, 95]
for score in scores:
    status = "PASS" if score >= 70 else "FAIL"
    print(f"{score}: {status}")

# Solution 3: Multiplication Table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}x{j}={i*j}", end=" ")
    print()

# Solution 4: Word Counter
text = "the quick brown fox jumps over the lazy dog the"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Solution 5: Normalization
raw_data = [100, 50, 75, 25, 90, 60]
min_val = min(raw_data)
max_val = max(raw_data)
normalized = [(x - min_val) / (max_val - min_val) for x in raw_data]
print(normalized)
