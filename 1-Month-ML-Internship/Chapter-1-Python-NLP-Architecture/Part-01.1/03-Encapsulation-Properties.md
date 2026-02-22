# 03: Encapsulation & Properties - Data Protection

**Duration:** 50 minutes | **Difficulty:** Intermediate | **Key Skill:** Data protection

---

## í¾¯ What You'll Learn

- Private vs public attributes
- Properties and @property decorator
- Getters and setters
- Data validation
- Encapsulation patterns

---

## í³š Data Protection

### Private Attributes (Naming Convention)

\`\`\`python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Private by convention
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        return self._balance
\`\`\`

### Properties with @property

\`\`\`python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value
\`\`\`

---

## í·  ML Context

\`\`\`python
class Model:
    def __init__(self, accuracy):
        self._accuracy = accuracy
    
    @property
    def accuracy(self):
        return self._accuracy
    
    @accuracy.setter
    def accuracy(self, val):
        if 0 <= val <= 1:
            self._accuracy = val
\`\`\`

---

## í´‘ Key Takeaways

âœ… Use _ prefix for private attributes
âœ… @property for custom getters
âœ… @setter for custom setters
âœ… Validate data in setters
âœ… Protect data integrity

---
