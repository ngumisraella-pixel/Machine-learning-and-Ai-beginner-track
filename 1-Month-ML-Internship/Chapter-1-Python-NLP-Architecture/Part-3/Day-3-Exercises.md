# Day 3: Exercises - Dynamic File Indexing & Vocabulary Building

**Date:** Week 1, Day 3 | **Estimated Time:** 3-4 hours | **Difficulty:** Foundational→Intermediate

---

## Exercise 1: File Operations with os and glob

Create `exercise1_file_operations.py`:

```python
# Exercise 1.1: Find all text files recursively
import os
import glob

corpus_dir = 'data/'
# TODO: Find all .txt files recursively using glob

# Exercise 1.2: Check file properties
# TODO: For each file, get size, creation date, extension

# Exercise 1.3: Organize files by directory
# TODO: Create dict: {directory: [files]}

# Exercise 1.4: Read all files into dictionary
# TODO: {filename: content} for all files

# Exercise 1.5: File statistics
# TODO: Total files, total size, average size
```

---

## Exercise 2: Building Dynamic Vocabularies

Create `exercise2_dynamic_vocabulary.py`:

```python
# Exercise 2.1: Implement DynamicVocabulary class
# TODO: add_word(), add_words(), get_index(), get_word()

# Exercise 2.2: Build vocabulary from multiple documents
documents = [
    "the quick brown fox",
    "the lazy dog",
    "quick brown dog"
]

# TODO: Build vocabulary and display word_to_index, index_to_word

# Exercise 2.3: Get frequency statistics
# TODO: Get top 10 words by frequency

# Exercise 2.4: Vocabulary size over time
# TODO: Show how vocabulary grows as documents are added
```

---

## Exercise 3: Document-to-ID Mapping

Create `exercise3_document_mapper.py`:

```python
# Exercise 3.1: Create bidirectional mapping
# TODO: word_to_index and index_to_word for sample corpus

# Exercise 3.2: Convert documents to ID vectors
# TODO: Map each document to vector of word indices

# Exercise 3.3: Build DocumentIndexer class
class DocumentIndexer:
    # TODO: Implement to index documents and maintain vocabulary
    pass

# Exercise 3.4: Index multiple documents
# TODO: Process corpus and create vocabulary

# Exercise 3.5: Export/Import vocabulary
# TODO: Save to JSON, verify by loading
```

---

## Exercise 4: JSON Serialization

Create `exercise4_json_serialization.py`:

```python
# Exercise 4.1: Serialize vocabulary
# TODO: Save word_to_index to JSON

# Exercise 4.2: Load and verify
# TODO: Load JSON and verify correctness

# Exercise 4.3: Handle special characters
# TODO: Ensure Unicode characters saved/loaded correctly

# Exercise 4.4: Save document metadata
# TODO: Save document counts, vocabulary size, etc.
```

---

## Exercise 5: Capstone - Document-to-ID Mapper

Create `exercise5_document_id_mapper_capstone.py`:

```python
class DocumentToIDMapper:
    """Complete document to ID mapping system"""
    
    # TODO: Implement:
    # - process_corpus(directory)
    # - get_document_info(doc_name)
    # - save_all(output_directory)
    # - export_vocabulary()
    # - build_document_vectors()

# Test with sample corpus:
# 1. Create sample text files
# 2. Process all files
# 3. Generate vocabulary
# 4. Create document vectors
# 5. Export to JSON
```

---

## Commit Strategy

```bash
git add exercise1_file_operations.py
git commit -m "feat: Complete Day 3 Exercise 1 - File Operations"

git add exercise2_dynamic_vocabulary.py
git commit -m "feat: Complete Day 3 Exercise 2 - Dynamic Vocabulary"

git add exercise3_document_mapper.py
git commit -m "feat: Complete Day 3 Exercise 3 - Document-to-ID Mapping"

git add exercise4_json_serialization.py
git commit -m "feat: Complete Day 3 Exercise 4 - JSON Serialization"

git add exercise5_document_id_mapper_capstone.py
git commit -m "feat: Complete Day 3 Exercise 5 - Document-to-ID Mapper (Capstone)"
```

---

**[← Back to Day 3 Module](./Day-3-File-Indexing.md)** | **[Day 4 Module →](./Day-4-Embeddings-Similarity.md)**
