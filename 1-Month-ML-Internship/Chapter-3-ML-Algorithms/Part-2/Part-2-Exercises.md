# Part 2: Classification & Logistic Regression - Exercises

**Difficulty:** Intermediate | **Time:** 6-7 hours | **Capstone:** Binary Classifier

---

## 📝 Exercise Set 1: Sigmoid & Probabilities

### Exercise 1.1: Implement Sigmoid
Create sigmoid function that:
- Takes any real number
- Returns probability [0, 1]
- Handles numerical overflow
- Plot the curve

**File:** `sigmoid_function.py`

---

### Exercise 1.2: Decision Boundaries
Create visualization showing:
- Different threshold values (0.5, 0.3, 0.7)
- How threshold changes decision boundary
- Impact on predictions

**File:** `decision_boundaries.py`

---

### Exercise 1.3: Cross-Entropy Loss
Implement cross-entropy loss:
- Compare with linear regression loss
- Show it penalizes wrong predictions heavily
- Visualize loss landscape

**File:** `cross_entropy_loss.py`

---

## 📝 Exercise Set 2: Binary Classification

### Exercise 2.1: Implement Logistic Regression
Create `LogisticRegression` class:
- Initialize weights randomly
- Implement gradient descent
- Predict probabilities
- Make binary predictions

**File:** `logistic_regression.py`

---

### Exercise 2.2: Classification Metrics
Implement from scratch:
- Confusion matrix
- Precision, Recall, F1 Score
- Accuracy
- ROC-AUC (optional)

**File:** `classification_metrics.py`

```python
def precision(y_true, y_pred):
    # TP / (TP + FP)
    pass

def recall(y_true, y_pred):
    # TP / (TP + FN)
    pass

def f1_score(y_true, y_pred):
    # 2 * (precision * recall) / (precision + recall)
    pass
```

---

### Exercise 2.3: Threshold Analysis
Create analysis showing:
- How different thresholds affect metrics
- Precision-Recall tradeoff
- Choose optimal threshold

**File:** `threshold_analysis.py`

---

## 📝 Exercise Set 3: Model Evaluation

### Exercise 3.1: Train/Test Split for Classification
Create function that:
- Splits balanced data properly
- Stratified split (maintains class ratio)
- Evaluates on both sets

**File:** `stratified_split.py`

---

### Exercise 3.2: Confusion Matrix Visualization
Create heatmap showing:
- True Positives, True Negatives
- False Positives, False Negatives
- Normalized and unnormalized

**File:** `confusion_matrix_viz.py`

---

### Exercise 3.3: ROC Curve (Optional Advanced)
Implement ROC curve:
- Plot True Positive Rate vs False Positive Rate
- Calculate AUC score
- Show optimal operating point

**File:** `roc_curve.py`

---

## 📝 Exercise Set 4: Multiclass Classification

### Exercise 4.1: One-vs-Rest Implementation
Create `MulticlassLogisticRegression`:
- Train binary classifier for each class
- Make multiclass predictions
- Handle probability normalization

**File:** `multiclass_logistic.py`

---

### Exercise 4.2: Multiclass Metrics
Implement multiclass versions:
- Macro-average precision/recall
- Micro-average precision/recall
- Per-class metrics

**File:** `multiclass_metrics.py`

---

### Exercise 4.3: Multiclass on Iris Dataset
Create classifier for Iris:
- Load Iris dataset (3 classes)
- Train multiclass model
- Evaluate all metrics
- Visualize with PCA (2D)

**File:** `iris_classifier.py`

---

## 📝 Exercise Set 5: Advanced Features

### Exercise 5.1: Feature Scaling Impact
Show how scaling affects logistic regression:
- Unscaled features
- Standardized features
- Normalized features
- Compare convergence

**File:** `scaling_impact_classification.py`

---

### Exercise 5.2: Imbalanced Data
Create experiment with imbalanced dataset:
- 90% class 0, 10% class 1
- Show accuracy deceiving
- Use precision/recall/F1 instead
- Show class weighting helps

**File:** `imbalanced_classification.py`

---

### Exercise 5.3: Hyperparameter Tuning
Grid search for:
- Learning rate
- Iteration count
- Threshold
- Find best combination

**File:** `hyperparameter_tuning_class.py`

---

## 🎯 Capstone: Binary Classifier

### Project: Build Complete Binary Classification System

**Scenario:**
Build spam email classifier or similar binary classification system.

**Deliverables:**

#### Part 1: Explore Data (`part1_explore.py`)
- Load classification dataset
- Class distribution analysis
- Feature statistics
- Check for imbalance

#### Part 2: Preprocess (`part2_preprocess.py`)
- Handle missing values
- Scale features
- Train/test split
- Handle imbalanced data (if needed)

#### Part 3: Build Model (`part3_build_model.py`)
```python
class BinaryClassifier:
    def fit(self, X, y):
        pass
    
    def predict(self, X):
        pass
    
    def predict_proba(self, X):
        pass
    
    def evaluate(self, y_true, y_pred):
        pass
```

#### Part 4: Train & Evaluate (`part4_train_evaluate.py`)
- Train on training set
- Evaluate on test set
- Report all metrics
- Visualize confusion matrix

#### Part 5: Scikit-learn Comparison (`part5_sklearn_comparison.py`)
```python
from sklearn.linear_model import LogisticRegression as SKLogReg

# Train both
# Compare predictions
# Compare metrics
# Verify match
```

#### Part 6: Report (`part6_report.py`)
```
BINARY CLASSIFICATION REPORT
=============================
Dataset: 1000 samples, 20 features
Classes: Class 0 (70%), Class 1 (30%)

Model: Logistic Regression (from scratch)

Training Results:
  - Accuracy: 0.92
  - Precision: 0.89
  - Recall: 0.85
  - F1 Score: 0.87

Testing Results:
  - Accuracy: 0.90
  - Precision: 0.87
  - Recall: 0.83
  - F1 Score: 0.85

Confusion Matrix (Test Set):
            Predicted
           Neg   Pos
Actual Neg [263   17]
       Pos [ 17   103]

ROC-AUC Score: 0.943

Key Findings:
- Model generalizes well
- Similar train/test performance
- Handles imbalance reasonably
- Matches scikit-learn results

Recommendations:
- Model ready for deployment
- Consider threshold tuning for business needs
- Monitor performance over time
```

**Success Criteria:**
- [ ] Binary classifier implemented
- [ ] All metrics calculated
- [ ] Train/test split proper
- [ ] Results match scikit-learn
- [ ] Evaluation complete
- [ ] Report generated

---

## 🔗 Navigation

**[← Back to Part 2 Module](./Part-2-Classification.md)** | **[Chapter 3 →](../README.md)**
