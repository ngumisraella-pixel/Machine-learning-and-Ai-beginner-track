# Chapter 1: Python & NLP Architecture

**Duration:** Week 1 | **Daily Time:** 7+ Hours | **Difficulty:** Foundational

---

## 🎯 Objective

Master the data structures and logic behind how machines 'read' human language. Learn advanced Python concepts and build the foundation for text processing.

---

## 📚 Weekly Overview

| Day | Topic | Focus | Capstone Task |
|-----|-------|-------|---------------|
| 1 | Data Structures & Functions | Lists, Dicts, Lambda, Comprehensions | Advanced Word Frequency Engine |
| 2 | Text Cleaning & Tokenization | Regex, Stopwords, N-grams | SimpleTokenizer Class |
| 3 | File Indexing & Vocabulary | Dynamic indexing, Bid-directional mapping | Document-to-ID Mapper |
| 4 | Embeddings & Similarity | One-Hot vectors, Dot Product, Cosine Similarity | Mini Embedding Engine |
| 5 | Integration & CLI | Combining all components, Modular design | Tiny NLP Engine (CLI) |

---

## 🎓 Learning Outcomes

By the end of Week 1, you will:

✅ Write efficient Python code using advanced data structures
✅ Clean and tokenize text data programmatically
✅ Build a vocabulary from raw text files
✅ Compute word embeddings manually
✅ Calculate similarity between text vectors
✅ Integrate multiple components into a complete system
✅ Create a CLI tool for text analysis

---

## 📖 Modules

### [Day 1: Advanced Python Data Structures & Functions](./Day-1-Advanced-Python.md)
Learn list comprehensions, lambda functions, and dictionary operations for text data.

**Key Concepts:**
- List comprehensions and nested structures
- Lambda functions and functional programming
- Dictionary operations for text counts
- Math module for numerical operations
- Edge case handling (encoding, line breaks)

**Capstone Task:** Advanced Word Frequency Engine

---

### [Day 2: Text Cleaning & NLP Preprocessing](./Day-2-Text-Preprocessing.md)
Master regex patterns, stopword removal, and n-gram generation.

**Key Concepts:**
- Regular expressions for pattern matching
- Stopword filtering logic
- N-gram generation (unigrams, bigrams, trigrams)
- Class-based tokenizer design
- Unicode and encoding handling

**Capstone Task:** SimpleTokenizer Class

---

### [Day 3: Dynamic File Indexing & Vocabulary Building](./Day-3-File-Indexing.md)
Build vocabulary systems from document collections.

**Key Concepts:**
- os and glob modules for file operations
- Dynamic vocabulary creation
- Bidirectional mapping systems (word ↔ index)
- Serialization to JSON
- Index management strategies

**Capstone Task:** Document-to-ID Mapper

---

### [Day 4: Embeddings & Similarity Computation](./Day-4-Embeddings-Similarity.md)
Manual implementation of vector embeddings and similarity metrics.

**Key Concepts:**
- One-hot vector representation
- Co-occurrence matrices
- Dot product calculations
- Cosine similarity from scratch
- Vector normalization

**Capstone Task:** Mini Embedding Engine

---

### [Day 5: NLP Pipeline Integration](./Day-5-NLP-Integration.md)
Combine all components into a production-ready system.

**Key Concepts:**
- Modular programming patterns
- Pipeline orchestration
- CLI design and argument parsing
- Error handling and logging
- Performance optimization

**Capstone Task:** Tiny NLP Engine (Complete CLI Tool)

---

## 🏗 Architecture Overview

```
Raw Text Files
    ↓
[Tokenizer] → SimpleTokenizer
    ↓
[Vocabulary Builder] → Document-to-ID Mapper
    ↓
[Embedding Engine] → One-Hot/Co-occurrence Vectors
    ↓
[Similarity Calculator] → Cosine Similarity
    ↓
CLI Interface → User Queries & Results
```

---

## 💻 Tools & Requirements

- **Python:** 3.8+
- **Libraries:** `re`, `math`, `json`, `glob`, `os`
- **No external ML libraries** - Build from scratch!
- **Git:** For version control and commits

---

## 📋 Assessment Criteria

| Criterion | Weight | Details |
|-----------|--------|---------|
| Code Quality | 30% | Clean code, proper naming, documentation |
| Logic Correctness | 40% | Algorithms work correctly on edge cases |
| Integration | 20% | Components work together seamlessly |
| Performance | 10% | Efficient algorithms and minimal runtime |

---

## 🚀 Getting Started

1. **Clone/Navigate** to this chapter's directory
2. **Read** each day's module overview
3. **Complete** all exercises for each day
4. **Commit** your work (detailed below)
5. **Progress** sequentially through all 5 days

---

## 📝 Commit Strategy

For each day:
```bash
# After finishing module content
git add Day-X-*.md
git commit -m "docs: Add Day X module content"

# After completing exercises
git add Day-X-Exercises.md
git commit -m "feat: Add comprehensive Day X exercises"
```

---

## ❓ Common Questions

**Q: Should I use external NLP libraries?**
A: No - the goal is algorithm intuition. Use only Python standard library for Week 1.

**Q: How do I handle large text files?**
A: Implement generators and file streaming to manage memory efficiently.

**Q: Can I use NumPy for Day 4?**
A: No - calculate vectors manually first. You'll use NumPy in Week 2+.

---

## 🔗 Navigation

**[← Back to Program Overview](../README.md)** | **[Start Day 1 →](./Day-1-Advanced-Python.md)**

---

**Ready to build NLP from first principles? Let's begin Week 1!**
