# Part 1: Linear Regression & Gradient Descent

**Week:** Week 3, Part 1 | **Duration:** 7+ Hours | **Difficulty:** Intermediate

---

## 🎯 Learning Objectives

By the end of Part 1, you will:

✅ Understand cost functions and loss metrics
✅ Implement gradient descent optimization
✅ Build linear regression models from scratch
✅ Tune hyperparameters (learning rate, iterations)
✅ Evaluate model performance with metrics
✅ Compare implementation with scikit-learn

---

## 📖 Core Topics

### 1. Linear Regression Fundamentals

#### The Problem
```python
# Given: dataset of (x, y) pairs
# Goal: find line y = mx + b that minimizes error

import numpy as np

# Sample data
X = np.array([1, 2, 3, 4, 5])  # Features
y = np.array([2, 4, 5, 4, 5])  # Targets

# We want to find optimal m and b
# such that prediction = m*x + b is close to actual y
```

#### Simple Linear Regression
```python
class SimpleLinearRegression:
    """Linear regression: y = m*x + b"""
    
    def __init__(self):
        self.m = 0  # slope
        self.b = 0  # intercept
    
    def fit(self, X, y):
        """Fit model using normal equation"""
        n = len(X)
        
        # Normal equation: m = (n*sum(xy) - sum(x)*sum(y)) / (n*sum(x²) - sum(x)²)
        m = (n * np.sum(X * y) - np.sum(X) * np.sum(y)) / \
            (n * np.sum(X**2) - np.sum(X)**2)
        
        # b = (sum(y) - m*sum(x)) / n
        b = (np.sum(y) - m * np.sum(X)) / n
        
        self.m = m
        self.b = b
        
        return self
    
    def predict(self, X):
        """Make predictions"""
        return self.m * X + self.b

# Usage
model = SimpleLinearRegression()
model.fit(X, y)
predictions = model.predict(X)
```

---

### 2. Cost Functions

#### Mean Squared Error (MSE)
```python
def mse(y_true, y_pred):
    """Calculate Mean Squared Error"""
    return np.mean((y_true - y_pred) ** 2)

# Usage
predictions = np.array([2.1, 4.0, 5.1, 3.9, 5.0])
actual = np.array([2, 4, 5, 4, 5])
loss = mse(actual, predictions)
print(f"MSE: {loss}")
```

#### Root Mean Squared Error (RMSE)
```python
def rmse(y_true, y_pred):
    """Calculate RMSE (same units as y)"""
    return np.sqrt(mse(y_true, y_pred))
```

#### Mean Absolute Error (MAE)
```python
def mae(y_true, y_pred):
    """Calculate Mean Absolute Error"""
    return np.mean(np.abs(y_true - y_pred))
```

#### R-Squared (Coefficient of Determination)
```python
def r_squared(y_true, y_pred):
    """Calculate R² score (0 to 1, higher is better)"""
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)
```

---

### 3. Gradient Descent

#### Understanding Gradients
```python
# The gradient tells us which direction to move
# to decrease the cost function

def gradient_mse(X, y, y_pred):
    """Calculate gradient of MSE loss"""
    # dL/dm = -2/n * sum(x * (y - y_pred))
    # dL/db = -2/n * sum(y - y_pred)
    
    n = len(y)
    errors = y - y_pred
    
    dm = -2/n * np.sum(X * errors)
    db = -2/n * np.sum(errors)
    
    return dm, db
```

#### Gradient Descent Implementation
```python
class LinearRegressionGD:
    """Linear regression using Gradient Descent"""
    
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.m = 0
        self.b = 0
        self.losses = []
    
    def fit(self, X, y):
        """Fit using gradient descent"""
        n = len(X)
        
        for i in range(self.iterations):
            # Predictions
            y_pred = self.m * X + self.b
            
            # Calculate gradients
            errors = y - y_pred
            dm = -2/n * np.sum(X * errors)
            db = -2/n * np.sum(errors)
            
            # Update parameters
            self.m -= self.lr * dm
            self.b -= self.lr * db
            
            # Calculate and store loss
            loss = np.mean(errors ** 2)
            self.losses.append(loss)
            
            # Print progress
            if (i + 1) % 100 == 0:
                print(f"Iteration {i+1}: Loss = {loss:.4f}")
        
        return self
    
    def predict(self, X):
        """Make predictions"""
        return self.m * X + self.b

# Usage
model = LinearRegressionGD(learning_rate=0.01, iterations=1000)
model.fit(X, y)
predictions = model.predict(X)
```

---

### 4. Feature Scaling

#### Why Scale?
```python
# Gradient descent converges faster with scaled features
# Different scales can cause issues (feature dominance)

def standardize(X):
    """Standardize features: (X - mean) / std"""
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std

def normalize(X):
    """Normalize to [0, 1]"""
    X_min = np.min(X, axis=0)
    X_max = np.max(X, axis=0)
    return (X - X_min) / (X_max - X_min)
```

---

### 5. Multiple Linear Regression

#### Matrix Form
```python
class MultipleLinearRegression:
    """Linear regression: y = X @ w (vector form)"""
    
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.w = None
        self.losses = []
    
    def fit(self, X, y):
        """Fit model using gradient descent"""
        # Add bias term
        X_with_bias = np.column_stack([np.ones(len(X)), X])
        
        # Initialize weights
        self.w = np.zeros(X_with_bias.shape[1])
        
        n = len(y)
        
        for i in range(self.iterations):
            # Predictions
            y_pred = X_with_bias @ self.w
            
            # Calculate gradient
            gradient = -2/n * X_with_bias.T @ (y - y_pred)
            
            # Update weights
            self.w -= self.lr * gradient
            
            # Calculate loss
            loss = np.mean((y - y_pred) ** 2)
            self.losses.append(loss)
        
        return self
    
    def predict(self, X):
        """Make predictions"""
        X_with_bias = np.column_stack([np.ones(len(X)), X])
        return X_with_bias @ self.w

# Usage
X_multi = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([5, 7, 9, 11, 13])

model = MultipleLinearRegression()
model.fit(X_multi, y)
predictions = model.predict(X_multi)
```

---

## 💡 Complete Example: Housing Price Predictor

```python
class HousingPricePredictor:
    """End-to-end housing price prediction"""
    
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.model = MultipleLinearRegression(lr, iterations)
        self.X_mean = None
        self.X_std = None
    
    def preprocess(self, X, fit=True):
        """Standardize features"""
        if fit:
            self.X_mean = np.mean(X, axis=0)
            self.X_std = np.std(X, axis=0)
        
        return (X - self.X_mean) / self.X_std
    
    def fit(self, X, y):
        """Fit model"""
        X_scaled = self.preprocess(X, fit=True)
        self.model.fit(X_scaled, y)
        return self
    
    def predict(self, X):
        """Make predictions"""
        X_scaled = self.preprocess(X, fit=False)
        return self.model.predict(X_scaled)
    
    def evaluate(self, y_true, y_pred):
        """Calculate evaluation metrics"""
        mse_val = np.mean((y_true - y_pred) ** 2)
        rmse_val = np.sqrt(mse_val)
        mae_val = np.mean(np.abs(y_true - y_pred))
        r2_val = r_squared(y_true, y_pred)
        
        return {
            'MSE': mse_val,
            'RMSE': rmse_val,
            'MAE': mae_val,
            'R²': r2_val
        }

# Usage
X_train = np.random.rand(100, 3) * 100  # 100 samples, 3 features
y_train = 50 + 0.5*X_train[:, 0] + 0.3*X_train[:, 1] - 0.2*X_train[:, 2]

predictor = HousingPricePredictor()
predictor.fit(X_train, y_train)
predictions = predictor.predict(X_train)
metrics = predictor.evaluate(y_train, predictions)
print(metrics)
```

---

## 🔗 Navigation

**[← Back to Chapter 3](../README.md)** | **[Part 1 Exercises →](./Part-1-Exercises.md)**
