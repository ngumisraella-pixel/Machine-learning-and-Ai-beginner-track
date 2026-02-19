# Part 1: Linear Regression & Gradient Descent - Exercises

**Difficulty:** Intermediate | **Time:** 6-7 hours | **Capstone:** Housing Price Predictor

---

## 📝 Exercise Set 1: Cost Functions

### Exercise 1.1: Implement Error Metrics
Create functions for:
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score

**File:** `error_metrics.py`

**Success Criteria:**
- [ ] All 4 metrics implemented
- [ ] Correct formula
- [ ] Return numeric values
- [ ] Handle edge cases

---

### Exercise 1.2: Compare Error Metrics
Create script that:
- Generates sample predictions vs actuals
- Calculates all 4 metrics
- Shows when each is useful
- Visualizes errors

**File:** `compare_metrics.py`

---

### Exercise 1.3: Loss Landscape Visualization
Create visualization that:
- Shows MSE for different m, b values
- Creates 3D surface plot
- Shows gradient direction
- Marks optimal solution

**File:** `loss_landscape.py`

---

## 📝 Exercise Set 2: Simple Linear Regression

### Exercise 2.1: Normal Equation Implementation
Implement `SimpleLinearRegression` class:
- Fit using normal equation
- Predict on new data
- Calculate R² score
- Handle edge cases

**File:** `simple_linear_regression.py`

---

### Exercise 2.2: Compare with NumPy
Compare your implementation with:
- `np.polyfit()` for 1-degree polynomial
- Show both give same results
- Compare performance

**File:** `compare_with_numpy.py`

---

### Exercise 2.3: Univariate Regression Analysis
Create analysis on sample dataset:
- Load data (or create synthetic)
- Fit model
- Make predictions
- Evaluate results

**File:** `univariate_analysis.py`

---

## 📝 Exercise Set 3: Gradient Descent

### Exercise 3.1: Implement Basic Gradient Descent
Create `LinearRegressionGD` class:
- Initialize parameters (m, b, lr, iterations)
- Calculate gradients
- Update parameters
- Track loss over time

**File:** `gradient_descent_basic.py`

```python
class LinearRegressionGD:
    def __init__(self, learning_rate=0.01, iterations=1000):
        pass
    
    def fit(self, X, y):
        # Fit using gradient descent
        pass
    
    def predict(self, X):
        pass
```

---

### Exercise 3.2: Learning Rate Effects
Create experiment that:
- Tests different learning rates
- Shows convergence behavior
- Visualizes loss curves
- Concludes optimal learning rate

**File:** `learning_rate_analysis.py`

---

### Exercise 3.3: Convergence Analysis
Create analysis showing:
- Loss decreases over iterations
- Convergence rate
- When model "stops improving"
- Early stopping criteria

**File:** `convergence_analysis.py`

---

## 📝 Exercise Set 4: Multiple Linear Regression

### Exercise 4.1: Vector-Based Linear Regression
Implement `MultipleLinearRegression`:
- Handle multiple features
- Add bias term (column of 1s)
- Implement matrix operations
- Make predictions

**File:** `multiple_linear_regression.py`

---

### Exercise 4.2: Feature Scaling Impact
Create experiment showing:
- GD without scaling (fails or slow)
- GD with standardization
- GD with normalization
- Compare convergence

**File:** `feature_scaling_impact.py`

---

### Exercise 4.3: Multivariate Analysis
Analyze multi-feature dataset:
- Load real data (100+ samples, 3+ features)
- Fit model
- Evaluate on train/test split
- Report metrics

**File:** `multivariate_analysis.py`

---

## 📝 Exercise Set 5: Model Evaluation

### Exercise 5.1: Train/Test Split
Create function that:
- Splits data into train/test (80/20)
- Fits on training data
- Evaluates on test data
- Reports both metrics

**File:** `train_test_split.py`

```python
def evaluate_model(X, y, test_size=0.2):
    """Split, train, evaluate"""
    # Split data
    # Train on training set
    # Evaluate on test set
    # Return metrics for both
    pass
```

---

### Exercise 5.2: Cross-Validation
Implement k-fold cross-validation:
- Split data into k folds
- Train on k-1, test on 1
- Repeat k times
- Report average performance

**File:** `cross_validation.py`

---

### Exercise 5.3: Hyperparameter Tuning
Create grid search that:
- Tests different learning rates
- Tests different iteration counts
- Finds best combination
- Reports results

**File:** `hyperparameter_tuning.py`

---

## 🎯 Capstone: Housing Price Predictor

### Project: Train and Evaluate Linear Regression Model

**Scenario:**
Build complete system to predict housing prices using linear regression.

**Deliverables:**

#### Part 1: Load & Explore Data (`part1_explore.py`)
```python
# Load housing dataset
# Explore features and target
# Show statistics
# Identify outliers
# Show correlations
```

#### Part 2: Preprocess Data (`part2_preprocess.py`)
```python
# Handle missing values
# Scale features
# Split train/test
# Save preprocessed data
```

#### Part 3: Build Model (`part3_build_model.py`)
```python
class HousingPricePredictor:
    def __init__(self, learning_rate=0.01, iterations=1000):
        pass
    
    def fit(self, X, y):
        pass
    
    def predict(self, X):
        pass
    
    def evaluate(self, y_true, y_pred):
        # Return dict with MSE, RMSE, MAE, R²
        pass
```

#### Part 4: Train and Evaluate (`part4_train_evaluate.py`)
```python
# Load preprocessed data
# Create model
# Fit on training data
# Evaluate on test data
# Show metrics
# Visualize predictions vs actuals
```

#### Part 5: Compare with Scikit-learn (`part5_sklearn_comparison.py`)
```python
from sklearn.linear_model import LinearRegression

# Train scikit-learn model
# Train your model
# Compare predictions
# Compare metrics
# Verify same results
```

#### Part 6: Analysis Report (`part6_report.py`)
```
HOUSING PRICE PREDICTION REPORT
================================
Dataset: 506 samples, 13 features
Target: Median house price

Model: Linear Regression (from scratch)

Training Metrics:
  - MSE: 21.89
  - RMSE: 4.68
  - MAE: 3.67
  - R²: 0.878

Testing Metrics:
  - MSE: 24.56
  - RMSE: 4.96
  - MAE: 3.90
  - R²: 0.865

Learning Curve:
  - Initial loss: 547.3
  - Final loss: 21.89
  - Converged at iteration: 987

Scikit-learn Comparison:
  - Results match ✓
  - Performance similar ✓

Top 5 Most Important Features:
  1. RM (rooms)
  2. LSTAT (lower status %)
  3. PTRATIO (pupil-teacher ratio)
  4. DIS (distance to employment)
  5. AGE (age of building)

Conclusions:
  - Model performs well (R² = 0.865)
  - Features properly scaled
  - GD converged successfully
  - Results match scikit-learn
```

**Success Criteria:**
- [ ] Model implementation correct
- [ ] Proper preprocessing
- [ ] Train/test split working
- [ ] All metrics calculated
- [ ] Results match scikit-learn
- [ ] Report generated
- [ ] Visualizations showing

---

## 📊 Sample Datasets

Use one of these datasets:
- **Housing Dataset:** Boston Housing prices (classic ML dataset)
- **Synthetic Data:** Generate linear data with noise
- **Real Data:** CSV with house prices

---

## 🔗 Navigation

**[← Back to Part 1 Module](./Part-1-Linear-Regression.md)** | **[Chapter 3 →](../README.md)**
