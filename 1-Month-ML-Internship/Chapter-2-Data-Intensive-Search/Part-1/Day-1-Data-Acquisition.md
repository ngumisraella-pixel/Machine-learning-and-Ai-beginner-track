# Day 1: Data Acquisition & Exploration

**Date:** Week 2, Day 1 | **Duration:** 7+ Hours | **Difficulty:** Foundational

---

## 🎯 Learning Objectives

By the end of Day 1, you will:

✅ Load and explore datasets from multiple formats (CSV, JSON)
✅ Understand data structure and data types
✅ Identify missing values, duplicates, and outliers
✅ Perform basic exploratory data analysis (EDA)
✅ Scrape HTML data using BeautifulSoup
✅ Handle real-world data messiness gracefully

---

## 📖 Core Topics

### 1. Working with Pandas DataFrames

#### Loading Data from CSV and JSON
```python
import pandas as pd

# Load CSV
df_csv = pd.read_csv('data.csv')

# Load JSON
df_json = pd.read_json('data.json')

# Load with specific parameters
df = pd.read_csv('data.csv', 
                  delimiter=',',
                  encoding='utf-8',
                  dtype={'age': int, 'salary': float},
                  na_values=['NA', 'N/A', ''])
```

#### Basic DataFrame Exploration
```python
import pandas as pd

df = pd.read_csv('customers.csv')

# Shape and info
print(df.shape)              # (rows, columns)
print(df.columns)            # Column names
print(df.dtypes)             # Data types
print(df.info())             # Detailed info

# First and last rows
print(df.head())             # First 5 rows
print(df.tail(10))           # Last 10 rows

# Summary statistics
print(df.describe())         # Numeric summary
print(df.describe(include='all'))  # All columns

# Column details
print(df['age'].value_counts())    # Value frequency
print(df['salary'].mean())         # Mean of column
```

#### Data Types Conversion
```python
# Convert column types
df['date'] = pd.to_datetime(df['date'])
df['age'] = df['age'].astype(int)
df['active'] = df['active'].astype(bool)

# Info on conversions
print(df.dtypes)
```

---

### 2. Handling Missing Values & Duplicates

#### Identifying Missing Data
```python
# Find missing values
print(df.isnull())           # Boolean mask
print(df.isnull().sum())     # Count per column
print(df.isnull().sum() / len(df) * 100)  # Percentage missing

# Visual: missing data heatmap would go here
```

#### Strategies for Missing Values
```python
# Drop rows with any missing
df_dropped = df.dropna()

# Drop rows where specific column is missing
df_dropped = df.dropna(subset=['salary'])

# Drop columns with all missing
df_dropped = df.dropna(axis=1, how='all')

# Fill missing with constant
df_filled = df.fillna(0)
df_filled = df.fillna({'salary': 0, 'bonus': 'N/A'})

# Forward/backward fill (for time series)
df_filled = df.fillna(method='ffill')  # Forward fill
df_filled = df.fillna(method='bfill')  # Backward fill

# Fill with aggregated values
df['salary'].fillna(df['salary'].mean(), inplace=True)
```

#### Identifying and Removing Duplicates
```python
# Check for duplicates
print(df.duplicated())       # Boolean mask
print(df.duplicated().sum()) # Count

# Check duplicates on specific columns
print(df.duplicated(subset=['email']))

# Remove duplicates
df_unique = df.drop_duplicates()
df_unique = df.drop_duplicates(subset=['email'])

# Keep first/last occurrence
df_unique = df.drop_duplicates(subset=['id'], keep='first')
```

---

### 3. Basic Web Scraping with BeautifulSoup

#### HTML Structure Basics
```python
from bs4 import BeautifulSoup
import requests

# Fetch HTML
response = requests.get('https://example.com')
html = response.text

# Parse HTML
soup = BeautifulSoup(html, 'html.parser')

# Find elements
title = soup.find('h1')              # First <h1>
titles = soup.find_all('h1')         # All <h1>
link = soup.find('a')['href']        # First link href

# CSS selectors
items = soup.select('.item')         # Class selector
items = soup.select('div > p')       # Child selector
```

#### Scraping Data into Lists
```python
from bs4 import BeautifulSoup
import requests

def scrape_products(url):
    """Scrape product information from HTML"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    products = []
    
    for item in soup.find_all('div', class_='product'):
        name = item.find('h2').text.strip()
        price = item.find('span', class_='price').text.strip()
        rating = item.find('span', class_='rating').text.strip()
        
        products.append({
            'name': name,
            'price': price,
            'rating': rating
        })
    
    return products

# Usage
products = scrape_products('https://example.com/products')
df = pd.DataFrame(products)
df.to_csv('products.csv', index=False)
```

---

### 4. Exploratory Data Analysis (EDA) Fundamentals

#### Basic EDA Class
```python
import pandas as pd
import numpy as np

class DataExplorer:
    """Class for basic data exploration"""
    
    def __init__(self, df):
        self.df = df
    
    def summary(self):
        """Print dataset summary"""
        print(f"Dataset Shape: {self.df.shape}")
        print(f"\nColumn Info:")
        print(self.df.info())
    
    def missing_report(self):
        """Report on missing values"""
        missing_count = self.df.isnull().sum()
        missing_pct = 100 * missing_count / len(self.df)
        
        missing_df = pd.DataFrame({
            'Column': missing_count.index,
            'Missing_Count': missing_count.values,
            'Missing_Percentage': missing_pct.values
        })
        
        return missing_df[missing_df['Missing_Count'] > 0]
    
    def duplicate_report(self):
        """Report on duplicate rows"""
        duplicates = self.df.duplicated().sum()
        print(f"Total Duplicates: {duplicates}")
        print(f"Percentage: {100 * duplicates / len(self.df):.2f}%")
    
    def numeric_summary(self):
        """Summary of numeric columns"""
        return self.df.describe()
    
    def categorical_summary(self):
        """Summary of categorical columns"""
        categorical_cols = self.df.select_dtypes(include='object').columns
        
        for col in categorical_cols:
            unique_count = self.df[col].nunique()
            most_common = self.df[col].value_counts().head(3)
            print(f"\n{col}:")
            print(f"  Unique values: {unique_count}")
            print(f"  Top 3 values:\n{most_common}")

# Usage
explorer = DataExplorer(df)
explorer.summary()
print(explorer.missing_report())
print(explorer.numeric_summary())
explorer.categorical_summary()
```

---

### 5. Data Quality Checks

#### Validation Functions
```python
def check_data_quality(df):
    """Comprehensive data quality check"""
    
    quality_report = {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'duplicate_rows': df.duplicated().sum(),
        'missing_values': df.isnull().sum().sum(),
        'numeric_columns': len(df.select_dtypes(include=['number']).columns),
        'categorical_columns': len(df.select_dtypes(include=['object']).columns)
    }
    
    return quality_report

def detect_outliers(df, column, method='iqr'):
    """Detect outliers using IQR method"""
    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        return outliers
    
    return df
```

---

## 💡 Complete Example: Data Acquisition Pipeline

```python
import pandas as pd
from bs4 import BeautifulSoup
import requests

class DataAcquisitionPipeline:
    """Complete data acquisition workflow"""
    
    def __init__(self, source_type='csv'):
        self.source_type = source_type
        self.df = None
    
    def load_csv(self, filepath):
        """Load data from CSV"""
        self.df = pd.read_csv(filepath)
        return self
    
    def load_json(self, filepath):
        """Load data from JSON"""
        self.df = pd.read_json(filepath)
        return self
    
    def scrape_html(self, url, selector):
        """Scrape data from HTML"""
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        data = []
        for element in soup.select(selector):
            data.append(element.text.strip())
        
        self.df = pd.DataFrame({'scraped_data': data})
        return self
    
    def clean(self):
        """Basic cleaning"""
        # Remove duplicates
        self.df = self.df.drop_duplicates()
        
        # Remove rows with all missing
        self.df = self.df.dropna(how='all')
        
        # Fill common missing values
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                self.df[col].fillna('Unknown', inplace=True)
            else:
                self.df[col].fillna(self.df[col].mean(), inplace=True)
        
        return self
    
    def explore(self):
        """Print exploration report"""
        print(f"Shape: {self.df.shape}")
        print(f"Columns: {list(self.df.columns)}")
        print(f"Missing: {self.df.isnull().sum().sum()}")
        print(f"Duplicates: {self.df.duplicated().sum()}")
        print(f"\nFirst few rows:")
        print(self.df.head())
        return self
    
    def save(self, filepath):
        """Save to CSV"""
        self.df.to_csv(filepath, index=False)
        print(f"Saved to {filepath}")
        return self
    
    def get_dataframe(self):
        """Return the dataframe"""
        return self.df

# Usage Example
pipeline = DataAcquisitionPipeline()
df = pipeline.load_csv('data.csv') \
    .clean() \
    .explore() \
    .save('cleaned_data.csv') \
    .get_dataframe()
```

---

## � Additional Resources & Learning Links

### **Pandas & Data Loading**
- **Pandas I/O Tools:** [pandas.pydata.org/docs/user_guide/io.html](https://pandas.pydata.org/docs/user_guide/io.html)
- **10 Minutes to Pandas:** [pandas.pydata.org/docs/user_guide/10min.html](https://pandas.pydata.org/docs/user_guide/10min.html)
- **Kaggle Pandas Course:** [kaggle.com/learn/pandas](https://www.kaggle.com/learn/pandas)

### **Web Scraping**
- **BeautifulSoup Docs:** [beautifulsoup4.readthedocs.io](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- **Real Python - Web Scraping:** [realpython.com/beautiful-soup-web-scraper](https://realpython.com/beautiful-soup-web-scraper-python/)

### **Data Exploration**
- **Kaggle EDA:** [kaggle.com/learn/data-visualization](https://www.kaggle.com/learn/data-visualization)
- **Exploratory Data Analysis:** [Wikipedia - EDA](https://en.wikipedia.org/wiki/Exploratory_data_analysis)

---

## �🔗 Navigation

**[← Back to Chapter 2](../README.md)** | **[Day 1 Exercises →](./Day-1-Exercises.md)**
