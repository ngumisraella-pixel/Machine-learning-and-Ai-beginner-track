# 10: Scope & Modules - Organizing Code

**Duration:** 50 minutes | **Difficulty:** Beginner | **Key Skill:** Code organization

---

## í¾¯ What You'll Learn

- Local vs global scope
- Understanding variable visibility
- Importing modules
- Using built-in modules

---

## í³š Scope

### Local Scope

\`\`\`python
def my_function():
    local_var = 10  # Local to function
    print(local_var)

my_function()  # Works
# print(local_var)  # ERROR - not accessible outside
\`\`\`

### Global Scope

\`\`\`python
global_var = 20  # Global

def access_global():
    print(global_var)  # Can access

access_global()  # Works - prints 20
\`\`\`

## í³š Modules

### Import Modules

\`\`\`python
import math
print(math.pi)

from math import sqrt
print(sqrt(16))

import numpy as np
\`\`\`

---

## í´‘ Key Takeaways

âœ… Local variables exist only in their function
âœ… Global variables accessible everywhere
âœ… Modules extend Python functionality
âœ… import brings in entire module
âœ… from...import brings specific items

---
