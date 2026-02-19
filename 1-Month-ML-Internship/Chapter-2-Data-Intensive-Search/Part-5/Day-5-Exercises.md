# Day 5: Streamlit Web Search Interface - Exercises

**Difficulty:** Intermediate | **Time:** 6-7 hours | **Capstone:** Full Micro Search Engine Web App

---

## 📝 Exercise Set 1: Streamlit Basics

### Exercise 1.1: Hello Streamlit
Create `hello_app.py`:
- Title and subheading
- Multiple text elements
- Display formatted text

```python
import streamlit as st

st.set_page_config(page_title="My App")
st.title("Hello Streamlit")
# Your code here
```

**File:** `01_hello_app.py`

---

### Exercise 1.2: Interactive Widgets
Create app with:
- Text input
- Number input
- Select box
- Checkbox
- Button

**File:** `02_interactive_widgets.py`

---

### Exercise 1.3: Data Display
Create app that displays:
- DataFrame
- Charts (simple plots)
- Metrics
- Columns layout

**File:** `03_data_display.py`

---

## 📝 Exercise Set 2: State Management

### Exercise 2.1: Session State
Create counter app:
- Initialize session state
- Increment/decrement buttons
- Display current value

**File:** `04_session_state.py`

---

### Exercise 2.2: Form State
Create form that:
- Collects user inputs
- Stores in session state
- Displays history of submissions

**File:** `05_form_state.py`

---

### Exercise 2.3: Caching
Create app that:
- Loads expensive data with `@st.cache_resource`
- Shows cache hit/miss
- Demonstrates performance benefit

**File:** `06_caching.py`

---

## 📝 Exercise Set 3: File Upload

### Exercise 3.1: Upload & Display CSV
Create app that:
- Accepts CSV upload
- Displays first rows
- Shows statistics

**File:** `07_csv_upload.py`

---

### Exercise 3.2: Process Uploaded Data
Create app that:
- Uploads CSV
- Applies transformations
- Downloads cleaned CSV

**File:** `08_process_upload.py`

---

### Exercise 3.3: Multiple File Upload
Create app that:
- Uploads multiple files
- Processes each
- Combines results

**File:** `09_multiple_upload.py`

---

## 📝 Exercise Set 4: Search Interface

### Exercise 4.1: Basic Search UI
Create search app with:
- Search box
- Submit button
- Display simple results

**File:** `10_basic_search.py`

---

### Exercise 4.2: Search with Options
Extend with:
- Sidebar for configuration
- Different search methods
- Result limit setting

**File:** `11_advanced_search.py`

---

### Exercise 4.3: Search Results Display
Create results page with:
- Ranked results
- Relevance scores
- Document preview
- Pagination (optional)

**File:** `12_search_results.py`

---

## 📝 Exercise Set 5: Complete App

### Exercise 5.1: Multi-Tab Interface
Create app with tabs for:
- Search
- Upload new documents
- Statistics
- Settings

**File:** `13_multi_tab_app.py`

---

### Exercise 5.2: Statistics Dashboard
Create dashboard showing:
- Total documents
- Total indexed terms
- Search statistics
- Popular queries

**File:** `14_statistics_dashboard.py`

---

### Exercise 5.3: Admin Interface
Create interface for:
- Adding documents
- Removing documents
- Rebuilding index
- Exporting index

**File:** `15_admin_interface.py`

---

## 🎯 Capstone: Complete Micro Search Engine Web App

### Project: Full-Featured Search Engine Web Application

**Deliverables:**

#### Part 1: Core App Structure (`app.py`)
```python
import streamlit as st
from pathlib import Path

# Configuration
st.set_page_config(
    page_title="Micro Search Engine",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme
st.markdown("""
<style>
    .main { max-width: 1200px; }
</style>
""", unsafe_allow_html=True)

# Main layout
```

#### Part 2: Search Page (`pages/01_search.py`)
Features:
- Search input box
- Search button
- Results display with:
  - Ranking/score
  - Document preview
  - Link to full document (optional)
- Filters:
  - Max results
  - Ranking method
  - Date range (if applicable)

```python
import streamlit as st
from search_engine import SearchEngine

st.title("🔍 Search")

# Load engine
@st.cache_resource
def get_engine():
    engine = SearchEngine()
    engine.load_documents('documents/')
    return engine

engine = get_engine()

# Search interface
query = st.text_input("Search query:")
col1, col2, col3 = st.columns(3)
max_results = col1.slider("Results", 5, 100, 10)
method = col2.radio("Method", ["TF-IDF", "Boolean"])
search_btn = col3.button("Search", type="primary")

if search_btn and query:
    # Search
    pass
```

#### Part 3: Upload Page (`pages/02_upload.py`)
Features:
- File upload (CSV or text files)
- Preview uploaded data
- Add to index button
- Confirmation message

```python
import streamlit as st

st.title("📤 Upload Documents")

uploaded_files = st.file_uploader("Upload files", type=["txt", "csv"])

if uploaded_files:
    # Process files
    st.success("Files added to index!")
```

#### Part 4: Statistics Page (`pages/03_statistics.py`)
Display:
- Total documents indexed
- Total unique terms
- Average document length
- Search performance metrics
- Charts (documents over time, term frequency, etc.)

```python
import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Statistics")

engine = get_engine()
stats = engine.get_statistics()

col1, col2, col3 = st.columns(3)
col1.metric("Documents", stats['documents'])
col2.metric("Terms", stats['terms'])
col3.metric("Avg Doc Length", f"{stats['avg_length']:.0f}")

# Charts
fig, ax = plt.subplots()
# Add chart
st.pyplot(fig)
```

#### Part 5: Settings Page (`pages/04_settings.py`)
Options for:
- Reconstruction index
- Export/import index
- Clear all data
- Search settings

```python
import streamlit as st

st.title("⚙️ Settings")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Index Management")
    if st.button("Rebuild Index"):
        # Rebuild
        st.success("Index rebuilt!")

with col2:
    st.subheader("Export/Import")
    if st.button("Export Index"):
        # Export
        st.download_button("Download Index", data, file_name="index.json")
```

#### Part 6: Supporting Modules

**search_engine.py** - Integration of Day 1-4 components:
```python
class SearchEngine:
    def __init__(self):
        self.index = PreprocessedInvertedIndex()
        self.tfidf_ranker = TFIDFSearchEngine(self.index)
    
    def load_documents(self, directory):
        # Load from directory
        pass
    
    def index_document(self, content):
        # Add to index
        pass
    
    def search(self, query, method='tfidf', top_k=10):
        if method == 'tfidf':
            return self.tfidf_ranker.ranked_search(query)
        else:
            # Boolean search
            pass
    
    def get_statistics(self):
        # Return stats
        pass
    
    def save_index(self, path):
        # Serialize
        pass
    
    def load_index(self, path):
        # Deserialize
        pass
```

#### Part 7: Run Instructions

**Directory structure:**
```
micro-search-engine/
├── app.py                    # Main app
├── search_engine.py          # Core logic
├── requirements.txt          # Dependencies
├── documents/                # Sample documents
│   ├── doc1.txt
│   ├── doc2.txt
│   └── ...
├── pages/
│   ├── 01_search.py
│   ├── 02_upload.py
│   ├── 03_statistics.py
│   └── 04_settings.py
└── README.md
```

**requirements.txt:**
```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
```

**Run:**
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎯 Success Criteria

- [ ] App runs without errors
- [ ] Search functionality works
- [ ] Results display correctly with scores
- [ ] Upload functionality works
- [ ] Statistics page shows accurate data
- [ ] Settings allow index management
- [ ] UI is clean and intuitive
- [ ] Performance is fast (< 1s for most searches)
- [ ] Can process multiple file formats
- [ ] Responsive layout

---

## 📝 Optional Enhancements

1. **Advanced Search**
   - Fuzzy matching
   - Synonym expansion
   - Query suggestions

2. **Visualization**
   - Search time trends
   - Popular queries chart
   - Term frequency visualization

3. **Persistence**
   - Save/load index to database
   - Search history
   - User preferences

4. **Deployment**
   - Deploy to Streamlit Cloud
   - Docker container
   - AWS/GCP deployment

---

## 🔗 Navigation

**[← Back to Day 5 Module](./Day-5-Streamlit-Search.md)** | **[Chapter 2 Complete! →](../README.md)**
