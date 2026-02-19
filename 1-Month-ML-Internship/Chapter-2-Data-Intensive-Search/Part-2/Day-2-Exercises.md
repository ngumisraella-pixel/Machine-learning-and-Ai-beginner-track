# Day 2: Feature Engineering & Data Transformation - Exercises

**Difficulty:** Foundational → Intermediate | **Time:** 6-7 hours | **Capstone:** Feature Engineering Lab

---

## 📝 Exercise Set 1: Label Encoding

### Exercise 1.1: Simple Label Encoder
Create a `LabelEncoder` class that:
- Takes categorical data in `fit()`
- Learns unique categories
- Encodes to integers in `transform()`
- Decodes back in `inverse_transform()`

**File:** `label_encoder.py`

```python
class LabelEncoder:
    def __init__(self):
        self.mapping = {}
        self.reverse_mapping = {}
    
    def fit(self, data):
        # Your implementation
        pass
    
    def transform(self, data):
        # Your implementation
        pass
    
    def fit_transform(self, data):
        return self.fit(data).transform(data)
    
    def inverse_transform(self, encoded_data):
        # Your implementation
        pass

# Usage
encoder = LabelEncoder()
colors = ['red', 'blue', 'green', 'red', 'blue']
encoded = encoder.fit_transform(colors)
decoded = encoder.inverse_transform(encoded)
```

**Success Criteria:**
- [ ] Encoding works correctly
- [ ] Decoding returns original values
- [ ] Handles unseen categories gracefully

---

### Exercise 1.2: Multi-Column Label Encoding
Create a function `encode_dataframe(df, columns)` that:
- Applies label encoding to specified columns
- Returns both encoded dataframe and mapping dict
- Preserves numeric columns unchanged

**File:** `encode_dataframe.py`

```python
def encode_dataframe(df, categorical_columns):
    """Encode multiple columns in a DataFrame"""
    df_encoded = df.copy()
    encoders = {}
    
    for col in categorical_columns:
        encoder = LabelEncoder()
        df_encoded[col] = encoder.fit_transform(df[col])
        encoders[col] = encoder
    
    return df_encoded, encoders

# Usage
df = pd.read_csv('data.csv')
df_encoded, encoders = encode_dataframe(df, ['department', 'city', 'gender'])
```

---

## 📝 Exercise Set 2: One-Hot Encoding

### Exercise 2.1: Build One-Hot Encoder
Create a `OneHotEncoder` class that:
- Learns categories from `fit()`
- Converts to binary matrix in `transform()`
- Returns column names for new features
- Handles unseen categories

**File:** `onehot_encoder.py`

```python
class OneHotEncoder:
    def __init__(self, handle_unknown='ignore'):
        self.categories = {}
        self.handle_unknown = handle_unknown
    
    def fit(self, data):
        # Learn unique categories
        pass
    
    def transform(self, data):
        # Convert to binary matrix
        pass
    
    def fit_transform(self, data):
        pass
    
    def get_feature_names(self):
        # Return names for encoded columns
        pass
```

**Success Criteria:**
- [ ] Binary matrix shape correct
- [ ] Values are 0 or 1
- [ ] Feature names match categories
- [ ] Unseen values handled

---

### Exercise 2.2: One-Hot Encoding with Sparse Matrix
Implement one-hot encoding using scipy's sparse matrices:
- Use `scipy.sparse.csr_matrix`
- Return sparse matrix instead of dense
- Report memory savings

**File:** `sparse_onehot_encoder.py`

**Challenge:** Handle DataFrames with millions of categories efficiently

---

### Exercise 2.3: Drop First Category
Modify encoder to drop first category to avoid multicollinearity:
- When encoding, skip the first category
- Reduces from n to n-1 columns
- Useful for linear models

**File:** `onehot_drop_first.py`

---

## 📝 Exercise Set 3: Feature Scaling

### Exercise 3.1: Implement StandardScaler
Create `StandardScaler` class that:
- Fits on training data
- Learns mean and std
- Transforms using these statistics
- Can transform new data

**File:** `standard_scaler.py`

```python
class StandardScaler:
    def __init__(self):
        self.mean = None
        self.std = None
    
    def fit(self, data):
        self.mean = np.mean(data)
        self.std = np.std(data)
        return self
    
    def transform(self, data):
        return (data - self.mean) / self.std
    
    def fit_transform(self, data):
        return self.fit(data).transform(data)
    
    def inverse_transform(self, scaled_data):
        return scaled_data * self.std + self.mean

# Usage
scaler = StandardScaler()
train_scaled = scaler.fit_transform(train_data)
test_scaled = scaler.transform(test_data)
predictions_original = scaler.inverse_transform(predictions_scaled)
```

**Success Criteria:**
- [ ] Scaled mean = 0, std = 1
- [ ] Inverse transform works
- [ ] Training/test separation correct

---

### Exercise 3.2: Implement MinMaxScaler
Create `MinMaxScaler` class that:
- Scales to [0, 1] range
- Learns min and max from training data
- Transforms using these bounds

**File:** `minmax_scaler.py`

**Bonus:** Handle case where min=max (single unique value)

---

### Exercise 3.3: Outlier-Safe Scaler
Create `RobustScaler` that:
- Uses median and interquartile range
- Less sensitive to outliers
- Scales to approximately [-1, 1]

**File:** `robust_scaler.py`

---

## 📝 Exercise Set 4: Building Feature Pipelines

### Exercise 4.1: Pipeline Manager
Create a `FeaturePipeline` class that:
- Chains multiple transformations
- Fits all transformers on training data
- Applies all transformations to new data

**File:** `feature_pipeline.py`

```python
class FeaturePipeline:
    def __init__(self):
        self.transformers = []
    
    def add(self, name, transformer):
        """Add transformer to pipeline"""
        self.transformers.append((name, transformer))
        return self
    
    def fit(self, df):
        """Fit all transformers"""
        for name, transformer in self.transformers:
            transformer.fit(df)
        return self
    
    def transform(self, df):
        """Apply all transformations"""
        result = df.copy()
        for name, transformer in self.transformers:
            result = transformer.transform(result)
        return result
    
    def fit_transform(self, df):
        return self.fit(df).transform(df)

# Usage
pipeline = FeaturePipeline()
pipeline.add('encode', OneHotEncoder())
pipeline.add('scale', StandardScaler())
X_transformed = pipeline.fit_transform(X)
```

---

### Exercise 4.2: Selective Transformation
Create a pipeline that:
- Applies different transformations to different columns
- Label encoding for tree models
- One-hot for linear models
- Scaling for neural networks

**File:** `selective_pipeline.py`

---

### Exercise 4.3: Column-Wise Pipelines
Implement pipelines that handle each column/column-type separately:
- Numeric → scale
- Categorical → encode
- DateTime → extract features

**File:** `column_pipelines.py`

---

## 📝 Exercise Set 5: ML Data Preparation

### Exercise 5.1: Train-Test-Appropriate Scaling
Create a function that:
- Splits data into train/test
- Fits scaler on training data only
- Applies to both train and test
- Demonstrates why train-fit-only is important

**File:** `train_test_scaling.py`

```python
def prepare_data_correctly(X, y, test_size=0.2):
    """Prepare data with proper train-test separation"""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test
```

**Key Lesson:** Never fit on test data!

---

### Exercise 5.2: Complete Data Preparation Class
Create class that:
- Handles train/test split
- Cleans data (missing, duplicates)
- Applies all transformations
- Returns ML-ready matrices

**File:** `ml_data_prep.py`

```python
class MLDataPreparator:
    def __init__(self, test_size=0.2):
        self.test_size = test_size
        self.scaler = StandardScaler()
        self.encoders = {}
    
    def fit(self, df, target_column):
        # Fit all transformers on training data
        pass
    
    def prepare(self, df, target_column):
        # Split, clean, transform
        pass

# Usage
prep = MLDataPreparator(test_size=0.2)
X_train, X_test, y_train, y_test = prep.prepare(df, target_column='target')
```

---

### Exercise 5.3: Feature Report Generator
Create function that reports:
- Original vs. transformed feature count
- Feature names and types after transformation
- Data shape before/after
- Recommendations

**File:** `feature_report.py`

---

## 🎯 Capstone: Feature Engineering Lab

### Project: Raw Dataset → ML-Ready Matrix

**Scenario:**
You're given `raw_sales_data.csv` with:
- Numeric features (price, quantity, discount)
- Categorical features (category, region, payment_method)
- DateTime feature (order_date)
- Missing values and outliers

**Deliverables:**

#### Part 1: Load & Explore (`part1_explore.py`)
```python
# Load the dataset
# Report initial statistics
# Identify data types and issues
# Show first few rows and shape
```

#### Part 2: Clean (`part2_clean.py`)
```python
def clean_data(df):
    """Handle missing values, duplicates, outliers"""
    # Handle missing values
    # Remove duplicates
    # Cap numerical outliers
    return df_clean
```

#### Part 3: Build Pipeline (`part3_pipeline.py`)
Create transformations:
```python
pipeline = FeaturePipeline()

# Add transformations based on feature types:
# 1. Handle DateTime → extract year, month, day_of_week
# 2. OneHotEncode categorical features
# 3. Scale numerical features
# 4. Handle encoded features

X = pipeline.fit_transform(df_clean)
```

#### Part 4: Prepare Train/Test (`part4_train_test.py`)
```python
def prepare_for_sklearn(X, y):
    """Return train/test split with proper scaling"""
    X_train, X_test, y_train, y_test = train_test_split(...)
    
    X_train_scaled = scale_train_test_properly(X_train, X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test
```

#### Part 5: Generate Report (`part5_report.py`)
Output comprehensive report:
```
FEATURE ENGINEERING REPORT
===========================
Raw Dataset: 10,000 rows, 12 columns
After Cleaning: 9,850 rows, 12 columns

Transformations Applied:
- DateTime: order_date → 4 features (year, month, day, dow)
- Categorical: 3 columns → 15 one-hot features
- Numerical: 5 columns scaled with StandardScaler
- Removed: 2 columns (>50% missing)

Result: 9,850 rows × 22 features (ML-Ready)

Train: 7,880 rows × 22
Test: 1,970 rows × 22

Feature Types:
- Numeric (scaled): 5
- One-hot encoded: 15
- DateTime-derived: 4

Ready for scikit-learn pipelines!
```

**Success Criteria:**
- [ ] All data types handled
- [ ] Train/test properly scaled
- [ ] No data leakage
- [ ] Report generated
- [ ] Data saved and ready

**Testing:**
```python
if __name__ == '__main__':
    df = pd.read_csv('raw_sales_data.csv')
    
    # Step by step
    df_clean = clean_data(df)
    X = pipeline.fit_transform(df_clean)
    X_train, X_test, y_train, y_test = prepare_for_sklearn(X, y)
    
    # Verify
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    
    # Can now use with sklearn:
    # model = LogisticRegression()
    # model.fit(X_train, y_train)
```

---

## 🔗 Navigation

**[← Back to Day 2 Module](./Day-2-Feature-Engineering.md)** | **[Chapter 2 →](../README.md)**
