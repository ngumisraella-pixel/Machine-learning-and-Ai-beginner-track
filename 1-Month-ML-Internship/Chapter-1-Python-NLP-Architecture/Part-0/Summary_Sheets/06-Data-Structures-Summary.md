# Data Structures Comparison

| Type | Mutable | Ordered | Unique | Use Case |
|------|---------|---------|--------|----------|
| List | ✓ | ✓ | ✗ | Collections, sequences |
| Tuple | ✗ | ✓ | ✗ | Dict keys, returns |
| Set | ✓ | ✗ | ✓ | Unique items, membership |
| Dict | ✓ | ✓ (3.7+) | ✓ keys | Labeled data, mappings |

## When to Use
- **List**: Default choice, can modify
- **Tuple**: Fixed data, use as dict key
- **Set**: Need unique values, fast lookup
- **Dict**: Need labels/keys for values

---
