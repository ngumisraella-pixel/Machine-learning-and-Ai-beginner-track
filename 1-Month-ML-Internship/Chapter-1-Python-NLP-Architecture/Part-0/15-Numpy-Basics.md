# 15: NumPy Basics - Numerical Computing Foundation

**Duration:** 60 minutes | **Difficulty:** Intermediate | **Key Skill:** ML essential library

---

## í¾¯ What You'll Learn

- NumPy arrays vs lists
- Creating arrays
- Array operations
- Universal functions
- Basic statistics

---

## í³š NumPy Arrays

\`\`\`python
import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4, 5])
zeros = np.zeros(5)  # [0. 0. 0. 0. 0.]
ones = np.ones(3)    # [1. 1. 1.]
range_arr = np.arange(0, 10, 2)  # [0 2 4 6 8]
\`\`\`

### Array Operations

\`\`\`python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
print(a + b)      # [5 7 9]
print(a * b)      # [4 10 18]
print(a ** 2)     # [1 4 9]
\`\`\`

### Statistics

\`\`\`python
scores = np.array([85, 92, 78, 95, 88])

mean = np.mean(scores)      # 87.6
std = np.std(scores)        # Statistical deviation
max_score = np.max(scores)  # 95
min_score = np.min(scores)  # 78
\`\`\`

---

## í·  ML Context

\`\`\`python
# Feature normalization
data = np.array([100, 50, 75, 25, 90])
normalized = (data - np.mean(data)) / np.std(data)
\`\`\`

---

## í´‘ Key Takeaways

âœ… NumPy arrays are faster than lists
âœ… Support element-wise operations
âœ… Essential for ML preprocessing
âœ… Vectorized operations are key
âœ… Statistical functions built-in

---
