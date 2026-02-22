# Decorator Patterns & Examples

## Simple Decorator
\`\`\`python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
\`\`\`

## With Arguments
\`\`\`python
def decorator(param):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator
\`\`\`

## Common Use Cases
- @property - convert method to attribute
- @classmethod - class-level methods
- @staticmethod - static methods
- @cache - result caching
- @wraps - preserve function metadata
