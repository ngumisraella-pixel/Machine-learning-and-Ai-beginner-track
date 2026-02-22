# 09: Regular Expressions - Pattern Matching for Text

**Duration:** 60 minutes | **Difficulty:** Intermediate | **Key Skill:** Text processing

---

## í¾¯ What You'll Learn

- Regex patterns and syntax
- Match, search, findall methods
- Substitution and splitting
- NLP applications

---

## í³š Regular Expressions

### Basic Patterns

\`\`\`python
import re

text = "Email: user@example.com"
pattern = r"[a-z]+@[a-z]+\.[a-z]+"

if re.search(pattern, text):
    print("Email found!")

emails = re.findall(pattern, text)
print(emails)
\`\`\`

### NLP Applications

\`\`\`python
# Tokenization
text = "Hello! How are you?"
tokens = re.findall(r"\b\w+\b", text)

# Clean text
text = "Hello123!!!World"
clean = re.sub(r"[^a-zA-Z\s]", "", text)
\`\`\`

---

## í´‘ Key Takeaways

âœ… Regex for pattern matching
âœ… Essential for text preprocessing
âœ… re.search, re.findall, re.sub
âœ… Critical for NLP tasks

---
