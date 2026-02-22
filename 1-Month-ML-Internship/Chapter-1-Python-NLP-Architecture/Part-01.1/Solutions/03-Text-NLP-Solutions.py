"""
Solutions for Exercise Set 3: Text and NLP Processing
"""

import re
from collections import Counter

# ===== BEGINNER SOLUTIONS =====

def validate_email(email):
    """Validate email using regex"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def count_words(text):
    """Count word frequencies"""
    words = re.findall(r"\b\w+\b", text.lower())
    return Counter(words)

# ===== INTERMEDIATE SOLUTIONS =====

def clean_text(text):
    """Clean text using regex"""
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def extract_entities(text):
    """Extract capitalized words as entities"""
    pattern = r"\b([A-Z][a-z]+)\b"
    return re.findall(pattern, text)

# ===== ADVANCED SOLUTIONS =====

def preprocess_text(text):
    """Full text preprocessing"""
    tokens = re.findall(r"\b\w+\b", text.lower())
    stopwords = {'the', 'a', 'an', 'and', 'or', 'but'}
    tokens = [t for t in tokens if t not in stopwords]
    return tokens

class Tokenizer:
    """Custom tokenizer with decorators and regex"""
    def __init__(self):
        self.vocab = {}
        self.word_to_idx = {}
        self.idx_to_word = {}
    
    def tokenize(self, text):
        """Tokenize using regex"""
        tokens = re.findall(r"\b\w+\b", text.lower())
        return tokens
    
    def get_vocabulary(self):
        """Build vocabulary"""
        self.vocab = list(set(self.word_to_idx.keys()))
        return self.vocab
    
    def convert_to_indices(self, tokens):
        """Convert tokens to indices"""
        return [self.word_to_idx.get(t, 0) for t in tokens]

if __name__ == "__main__":
    print(validate_email("test@example.com"))
    print(count_words("hello world hello"))
    print(clean_text("Hello, World! This is TEXT."))
