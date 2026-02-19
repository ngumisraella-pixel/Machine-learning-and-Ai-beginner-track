# Day 3: Dynamic File Indexing & Vocabulary Building

**Date:** Week 1, Day 3 | **Duration:** 7+ Hours | **Difficulty:** Foundational→Intermediate

---

## 🎯 Learning Objectives

✅ Master os and glob modules for file operations
✅ Create dynamic vocabulary systems from document collections  
✅ Build bidirectional mappings (word ↔ index)
✅ Serialize vocabularies to JSON
✅ Implement document-level indexing
✅ Optimize vocabulary management for large collections

---

## 📖 Core Topics

### 1. File Handling with os and glob

```python
import os
import glob

# Find all files in directory
text_files = glob.glob('data/*.txt')
# Recursive search
all_texts = glob.glob('data/**/*.txt', recursive=True)

# Check file existence and size
if os.path.exists('file.txt'):
    size = os.path.getsize('file.txt')
    print(f"File size: {size} bytes")

# List directory contents
for filename in os.listdir('data/'):
    filepath = os.path.join('data/', filename)
    if os.path.isfile(filepath):
        print(f"File: {filename}")

# Extract filename without extension
filename = os.path.basename('path/to/file.txt')
stem = os.path.splitext(filename)[0]
```

### 2. Building Dynamic Vocabularies

```python
class DynamicVocabulary:
    """Build vocabulary from document collections"""
    
    def __init__(self):
        self.word_to_index = {}
        self.index_to_word = {}
        self.word_freq = {}
        self.next_index = 0
    
    def add_word(self, word):
        """Add word to vocabulary"""
        word = word.lower()
        if word not in self.word_to_index:
            self.word_to_index[word] = self.next_index
            self.index_to_word[self.next_index] = word
            self.next_index += 1
        
        self.word_freq[word] = self.word_freq.get(word, 0) + 1
    
    def add_words(self, words):
        """Add multiple words"""
        for word in words:
            self.add_word(word)
    
    def get_index(self, word):
        """Get index for word (returns None if not found)"""
        return self.word_to_index.get(word.lower())
    
    def get_word(self, index):
        """Get word by index"""
        return self.index_to_word.get(index)
    
    def size(self):
        """Get vocabulary size"""
        return len(self.word_to_index)
    
    def get_top_words(self, n=100):
        """Get top N most frequent words"""
        sorted_words = sorted(
            self.word_freq.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return sorted_words[:n]
```

### 3. Bidirectional Mapping

```python
def create_bidirectional_mapping(words):
    """Create word ↔ index mappings"""
    word_to_index = {word: i for i, word in enumerate(set(words))}
    index_to_word = {i: word for word, i in word_to_index.items()}
    return word_to_index, index_to_word

# Usage
words = ['apple', 'banana', 'cherry', 'apple', 'date']
w2i, i2w = create_bidirectional_mapping(words)
print(w2i)  # {'apple': 0, 'banana': 1, ...}
print(i2w)  # {0: 'apple', 1: 'banana', ...}
```

### 4. JSON Serialization

```python
import json

def save_vocabulary(vocab, filepath):
    """Save vocabulary to JSON"""
    data = {
        'word_to_index': vocab.word_to_index,
        'vocabulary_size': vocab.size(),
        'word_frequencies': vocab.word_freq
    }
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_vocabulary(filepath):
    """Load vocabulary from JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
```

### 5. Document Indexing System

```python
class DocumentIndexer:
    """Index all documents and create vocabulary"""
    
    def __init__(self):
        self.vocabulary = DynamicVocabulary()
        self.documents = {}  # filename -> tokens
        self.doc_vocab_vectors = {}  # filename -> vector
    
    def index_document(self, filepath, tokenizer):
        """Process and index a single document"""
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        
        tokens = tokenizer.process(text)
        doc_name = os.path.basename(filepath)
        
        self.documents[doc_name] = tokens
        self.vocabulary.add_words(tokens)
    
    def index_directory(self, directory, tokenizer, pattern='*.txt'):
        """Index all documents in directory"""
        files = glob.glob(os.path.join(directory, pattern))
        for filepath in files:
            try:
                self.index_document(filepath, tokenizer)
            except Exception as e:
                print(f"Error indexing {filepath}: {e}")
    
    def get_document_vector(self, doc_name):
        """Convert document to index vector"""
        if doc_name not in self.documents:
            return None
        
        tokens = self.documents[doc_name]
        vector = [self.vocabulary.get_index(t) for t in tokens]
        return vector
    
    def export_vocabulary(self, filepath):
        """Save vocabulary to JSON"""
        data = {
            'word_to_index': self.vocabulary.word_to_index,
            'index_to_word': {str(k): v for k, v in self.vocabulary.index_to_word.items()},
            'size': self.vocabulary.size(),
            'frequencies': self.vocabulary.word_freq
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
```

---

## 💡 Complete Example

```python
class DocumentToIDMapper:
    """Complete document → ID mapping system"""
    
    def __init__(self):
        self.indexer = DocumentIndexer()
        self.tokenizer = SimpleTokenizer(lowercase=True, remove_stopwords=True)
    
    def process_corpus(self, corpus_dir):
        """Process entire document collection"""
        self.indexer.index_directory(corpus_dir, self.tokenizer)
        return {
            'vocab_size': self.indexer.vocabulary.size(),
            'doc_count': len(self.indexer.documents),
            'top_words': self.indexer.vocabulary.get_top_words(20)
        }
    
    def get_document_info(self, doc_name):
        """Get info about specific document"""
        if doc_name not in self.indexer.documents:
            return None
        
        tokens = self.indexer.documents[doc_name]
        vector = self.indexer.get_document_vector(doc_name)
        
        return {
            'token_count': len(tokens),
            'unique_tokens': len(set(tokens)),
            'vector': vector,
            'vector_length': len(vector)
        }
    
    def save_all(self, output_dir):
        """Save vocabulary and document vectors"""
        self.indexer.export_vocabulary(os.path.join(output_dir, 'vocabulary.json'))
        
        # Save document vectors
        doc_vectors = {}
        for doc in self.indexer.documents:
            doc_vectors[doc] = self.indexer.get_document_vector(doc)
        
        with open(os.path.join(output_dir, 'document_vectors.json'), 'w') as f:
            json.dump(doc_vectors, f, indent=2)
```

---

**[← Back to Chapter 1](./README.md)** | **[Day 3 Exercises →](./Day-3-Exercises.md)**
