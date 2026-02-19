# Chapter 3: Machine Learning Algorithms

**Week:** Week 3 | **Duration:** 5 Parts (35+ hours) | **Level:** Intermediate

---

## 🎯 Chapter Objective

Master fundamental ML algorithms by implementing them **from scratch** before using libraries.

By the end of this chapter, you will:
- ✅ Implement linear regression with gradient descent
- ✅ Build classification models (Logistic Regression)
- ✅ Construct decision trees and random forests
- ✅ Cluster data with K-means and DBSCAN
- ✅ Reduce dimensionality with PCA
- ✅ Understand when to use each algorithm

---

## 📋 Weekly Structure

| Part | Topic | Core Concepts | Capstone |
|------|-------|---------------|----------|
| **1** | Linear Regression | Loss functions, Gradient descent, Optimization | Housing Price Predictor |
| **2** | Classification | Logistic regression, Decision boundaries, Metrics | Binary Classifier |
| **3** | Tree-Based Models | Decision trees, Ensembles, Random forests | Forest Classifier |
| **4** | Clustering | K-means, DBSCAN, Silhouette analysis | Document Clustering |
| **5** | Dimensionality Reduction | PCA, Variance explained, Visualization | ML Pipeline |

---

## 🏗️ Architecture Philosophy

**Progressive Complexity:** Build algorithms from first principles

- **Part 1:** Understand optimization (gradient descent)
- **Part 2:** Extend to classification
- **Part 3:** Ensemble methods (combine weak learners)
- **Part 4:** Unsupervised learning
- **Part 5:** Model selection and pipelines

**Key Principle:** Math → Code → Scikit-learn comparison

---

## 📂 Directory Structure

```
Chapter-3-ML-Algorithms/
├── README.md (this file)
├── Part-1/
│   ├── Part-1-Linear-Regression.md
│   └── Part-1-Exercises.md
├── Part-2/
│   ├── Part-2-Classification.md
│   └── Part-2-Exercises.md
├── Part-3/
│   ├── Part-3-Decision-Trees.md
│   └── Part-3-Exercises.md
├── Part-4/
│   ├── Part-4-Clustering.md
│   └── Part-4-Exercises.md
└── Part-5/
    ├── Part-5-Dimensionality-Reduction.md
    └── Part-5-Exercises.md
```

---

## 🎓 Learning Outcomes

### By Part 1 (Linear Regression)
- Understand cost functions (MSE)
- Implement gradient descent
- Build simple linear models
- Tune learning rate and iterations

### By Part 2 (Classification)
- Extend regression to classification
- Implement logistic regression
- Calculate decision boundaries
- Evaluate with precision/recall/F1

### By Part 3 (Tree-Based)
- Build decision trees from scratch
- Understand feature importance
- Implement random forests (bagging)
- Compare with scikit-learn

### By Part 4 (Clustering)
- Implement K-means algorithm
- Determine optimal K (elbow method)
- Understand DBSCAN
- Evaluate clustering quality

### By Part 5 (Dimensionality Reduction)
- Implement PCA
- Reduce data dimensions
- Visualize high-dimensional data
- Build complete ML pipelines

---

## 🔧 Technologies and Libraries

### Core Math
```python
NumPy          # Matrix operations
Math           # Basic mathematics
```

### ML Libraries (for comparison)
```python
Scikit-learn   # Production models
```

### Visualization
```python
Matplotlib     # Plotting results
```

---

## 💡 Real-World Applications

1. **Housing Price Prediction** (Part 1)
   - Linear regression on house features
   - Predicting continuous values

2. **Customer Classification** (Part 2)
   - Binary/multiclass classification
   - Predicting customer categories

3. **Decision Tree Classification** (Part 3)
   - Interpretable models
   - Feature importance analysis

4. **Document Clustering** (Part 4)
   - Grouping similar documents
   - Customer segmentation

5. **Feature Extraction** (Part 5)
   - Reducing dimensionality
   - Visualization of complex data

---

## 📊 Assessment Criteria

### Part Exercises (40%)
- Correct algorithm implementation
- Code efficiency and clarity
- Proper error handling

### Part Capstones (60%)
- Working model on real data
- Proper evaluation metrics
- Comparison with scikit-learn

### Bonus (Extra Credit)
- Advanced optimization techniques
- Hyperparameter tuning
- Cross-validation implementation

---

## 🚀 Quick Start

### Prerequisites
```bash
pip install numpy scikit-learn matplotlib pandas
```

### Workflow
1. Study the Part module content
2. Implement algorithm from scratch
3. Complete exercises
4. Build capstone project
5. Compare with scikit-learn implementation

---

## 📚 Core Concepts Map

```
PART 1: LINEAR REGRESSION
  Cost Function → Gradient Descent → Parameter Update
  
PART 2: CLASSIFICATION (Extends Part 1)
  Logistic Function → Cross-Entropy Loss → Decision Boundary
  
PART 3: TREE-BASED MODELS
  Information Gain → Tree Construction → Ensemble (Random Forest)
  
PART 4: CLUSTERING (Unsupervised)
  Distance Metrics → K-means Algorithm → Cluster Validation
  
PART 5: DIMENSIONALITY REDUCTION
  Covariance Matrix → Eigendecomposition → PCA Projection
```

---

## 🔗 Navigation

- **[← Back to Main](../README.md)**
- **[Part 1: Linear Regression →](./Part-1/)**

---

## 💬 Key ML Principles

1. **Supervised vs Unsupervised**
   - Parts 1-3: Supervised (labels provided)
   - Part 4: Unsupervised (no labels)
   - Part 5: Feature extraction (both)

2. **Bias-Variance Tradeoff**
   - Complex models overfit
   - Simple models underfit
   - Find balance

3. **Model Evaluation**
   - Train/test split essential
   - Use appropriate metrics
   - Cross-validation for robustness

4. **Feature Importance**
   - Not all features equal
   - Proper scaling needed
   - Feature selection crucial

5. **Algorithm Selection**
   - Linear data → linear models
   - Complex patterns → trees/forests/neural nets
   - High dimensions → dimensionality reduction

---

**Last Updated:** February 19, 2026 | **Status:** Ready for implementation
