# Part 3: Jupyter Notebooks & IDEs

**Duration:** 2-3 hours | **Level:** Beginner | **Prerequisites:** Part 1-2 (Python & Git setup)

---

## 📚 Overview

You'll spend most of your time writing Python code in:
1. **Jupyter Notebooks** - For experimentation and learning
2. **IDE (VS Code/PyCharm)** - For projects and final code

This Part covers both tools and how to choose between them.

---

## 🎯 Learning Outcomes

By the end of this Part, you will:
- ✅ Install and use Jupyter Notebook
- ✅ Create interactive Python notebooks
- ✅ Install and configure VS Code for Python
- ✅ Know when to use notebooks vs. IDEs
- ✅ Set up your preferred development environment

---

## 📓 Part 1: Jupyter Notebooks

### **What are Jupyter Notebooks?**

Jupyter Notebooks combine **code, text, visualizations, and math** in one interactive document.

**Perfect for:**
- Learning and experimentation
- Data exploration
- Visualization
- Tutorials and documentation

**Not ideal for:**
- Large production projects
- Complex code organization
- Team collaboration (difficult with version control)

### **Installation**

Jupyter comes with Anaconda or can be installed via pip:

```bash
# With virtual environment active
pip install jupyter
```

### **Starting Jupyter**

```bash
# From your project directory
jupyter notebook

# Or use Jupyter Lab (more modern)
pip install jupyterlab
jupyter lab
```

This opens a web browser at `http://localhost:8888` with your file explorer.

### **Creating Your First Notebook**

1. Click "New" → "Python 3"
2. A new blank notebook opens
3. You now have **cells** where you can type code or text

### **Notebook Basics**

**Code Cell:**
```python
# This is a code cell
x = 5
print(x ** 2)
```
- Press `Shift + Enter` to run the cell
- Output appears below the cell

**Markdown Cell:**
```markdown
# This is a heading
This is text with **bold** and *italic*.
```
- Press `Shift + Enter` to format the text
- Great for explanations and documentation

### **Example Notebook: Linear Regression Learning**

```python
# Cell 1: Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Cell 2: Generate synthetic data
X = np.linspace(0, 10, 50)
y = 2 * X + 1 + np.random.randn(50) * 2  # y = 2x + 1 + noise

print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")

# Cell 3: Implement gradient descent
def gradient_descent(X, y, learning_rate=0.01, iterations=1000):
    m = len(X)
    w = 0.0  # weight
    b = 0.0  # bias
    
    for i in range(iterations):
        # Predictions
        y_pred = w * X + b
        
        # Errors
        error = y_pred - y
        
        # Gradients
        dw = (2/m) * np.sum(X * error)
        db = (2/m) * np.sum(error)
        
        # Update parameters
        w -= learning_rate * dw
        b -= learning_rate * db
        
        if i % 200 == 0:
            loss = np.mean(error ** 2)
            print(f"Iteration {i}: Loss = {loss:.4f}")
    
    return w, b

# Cell 4: Train the model
w, b = gradient_descent(X, y)
print(f"\nFinal: w={w:.4f}, b={b:.4f}")

# Cell 5: Visualize results
y_pred = w * X + b
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.5, label='Actual data')
plt.plot(X, y_pred, color='red', linewidth=2, label='Fitted line')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression')
plt.show()
```

### **Keyboard Shortcuts**

| Shortcut | Action |
|----------|--------|
| `Shift + Enter` | Run current cell |
| `Ctrl + Enter` | Run cell, stay on cell |
| `Alt + Enter` | Run cell, insert new cell below |
| `A` | Insert cell above (command mode) |
| `B` | Insert cell below (command mode) |
| `D D` | Delete cell (command mode) |
| `M` | Change to Markdown (command mode) |
| `Y` | Change to Code (command mode) |

### **Saving Notebooks**

Jupyter auto-saves every few seconds, but you can:
```bash
# Save manually
Ctrl + S

# Your notebook: filename.ipynb
```

---

## 💻 Part 2: VS Code Setup

### **Why VS Code?**

VS Code is a lightweight, powerful code editor ideal for:
- Writing Python projects
- Debugging code
- Integration with Git
- Terminal access
- Multiple file management

### **Installation**

1. Go to [code.visualstudio.com](https://code.visualstudio.com/)
2. Download for your OS
3. Install (accept defaults)
4. Open VS Code

### **Essential VS Code Extensions for Python**

Open VS Code and install these extensions:

1. **Python** (Microsoft)
   - Go to Extensions (Ctrl + Shift + X)
   - Search "Python"
   - Install the official Microsoft extension
   - Provides: syntax highlighting, debugging, linting

2. **Pylance** (Microsoft)
   - Install from Extensions
   - Provides: code completion, type checking, smart suggestions

3. **Jupyter** (Microsoft)
   - Allows running Jupyter notebooks in VS Code
   - Provides: interactive cell execution

4. **GitLens** (Optional)
   - Helps visualize Git history
   - Shows who changed what and when

### **VS Code Configuration**

#### **Configure Python Interpreter**

1. Press `Ctrl + Shift + P` (Command Palette)
2. Type "Python: Select Interpreter"
3. Choose the one in your `ml_internship` virtual environment
4. It should show path like `./ml_internship/bin/python`

#### **Create VS Code Settings**

In your project root, create `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/ml_internship/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "[python]": {
        "editor.formatOnSave": true,
        "editor.insertSpaces": true,
        "editor.tabSize": 4
    }
}
```

### **VS Code Workflow**

1. **Open Folder** - File → Open Folder → Select `seedai/`
2. **Create File** - Right-click → New File → `script.py`
3. **Run File** - Press `F5` or click Run button
4. **Debug** - Set breakpoints (click line number), press `F5`
5. **Terminal** - Press `` Ctrl + ` `` to open integrated terminal

### **Example: Running a Python Script**

Create `hello_ml.py`:

```python
"""
Simple script to test VS Code Python setup.
"""

import numpy as np

def calculate_stats(data):
    """Calculate mean and standard deviation."""
    mean = np.mean(data)
    std = np.std(data)
    return mean, std

if __name__ == "__main__":
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    mean, std = calculate_stats(data)
    
    print(f"Data: {data}")
    print(f"Mean: {mean:.2f}")
    print(f"Std Dev: {std:.2f}")
```

Run in VS Code:
- Press `F5` or click "Run" triangle
- Output appears in integrated terminal

---

## 🤔 Part 3: Notebooks vs. IDEs - Which to Use?

### **Use Jupyter Notebook When:**
✅ Learning new concepts  
✅ Exploring data  
✅ Creating visualizations  
✅ Quick experimentation  
✅ Teaching/tutorials  

### **Use VS Code IDE When:**
✅ Building projects  
✅ Writing production code  
✅ Large codebase  
✅ Team collaboration  
✅ Running tests  

### **Hybrid Workflow (Recommended)**

```
Learning Phase          →  Jupyter Notebook
Understand concepts     →  Write code cells
Visualize results       →  See plots inline
--------
Implementation Phase   →  VS Code
Organize code          →  Project structure
Refactor code          →  Multiple files
Test thoroughly        →  Unit tests
Deploy                 →  Final scripts
```

---

## 📊 Recommended Setup for This Course

| Phase | Tool | Reason |
|-------|------|--------|
| **Part Reading** | Jupyter Notebook | Interactive learning |
| **Part Exercises** | VS Code (or Notebook) | Clean code organization |
| **Part Capstone** | VS Code | Professional project structure |
| **Debugging Issues** | VS Code + Debugger | Better debugging tools |

---

## 🔗 Additional Resources

### **Jupyter Documentation:**
- **Official Jupyter:** [jupyter.org](https://jupyter.org/)
  - Overview and installation guide
  
- **Jupyter Notebook Docs:** [jupyter-notebook.readthedocs.io](https://jupyter-notebook.readthedocs.io/)
  - Complete reference

- **Jupyter Tips & Tricks:** [Real Python - Jupyter Notebook](https://realpython.com/jupyter-notebook-introduction/)
  - Pro tips for efficient notebooks

### **VS Code Python Development:**
- **VS Code Python Tutorial:** [code.visualstudio.com/docs/python](https://code.visualstudio.com/docs/python/python-tutorial)
  - Official VS Code Python guide
  
- **VS Code Debugging:** [code.visualstudio.com/docs/python/debugging](https://code.visualstudio.com/docs/python/debugging)
  - Debug Python code in VS Code

- **VS Code Keyboard Shortcuts:** [code.visualstudio.com/docs/getstarted/keybindings](https://code.visualstudio.com/docs/getstarted/keybindings)
  - Essential shortcuts reference

### **Interactive Learning:**
- **Official Jupyter Tutorial:** [Try Jupyter Online](https://try.jupyter.org/)
  - Try Jupyter in your browser (no install needed)

- **Kaggle Notebooks:** [kaggle.com/notebooks](https://kaggle.com/notebooks)
  - See thousands of example Jupyter notebooks
  - Learn from real data science projects

### **Best Practices:**
- **Writing Good Notebooks:** [Guillermo Carrasco - Guide to Jupyter Notebooks](https://www.guillermo-carrasco.com/posts/how-to-share-jupyter-notebooks-on-github/)
  - Make your notebooks production-ready
  
- **Clean Code in Python:** [Real Python - PEP 8](https://realpython.com/pep-8-style-guide-for-python-code/)
  - Write code that's readable and professional

---

## ✅ Success Criteria

You've successfully completed Part 3 when:

- [ ] Jupyter Notebook installed and running
- [ ] Created your first Jupyter notebook
- [ ] Code and Markdown cells both work
- [ ] VS Code installed with Python extension
- [ ] Python interpreter configured in VS Code
- [ ] Can run Python scripts in VS Code
- [ ] Understand when to use notebooks vs. IDE
- [ ] Have your preferred development environment set up

---

## 🎓 Next Steps

Once you've completed this Part:
→ Move to **Part 4: ML Libraries Overview** to understand the tools you'll use

---

**Part Status:** ✅ Complete  
**Difficulty:** ⭐⭐ (Beginner-Intermediate)  
**Time Estimate:** 2-3 hours  
**Key Takeaway:** Jupyter Notebooks and VS Code are complementary tools for different phases of learning and development.
