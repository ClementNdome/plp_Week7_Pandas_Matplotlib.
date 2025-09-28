"# plp_Week7_Pandas_Matplotlib." 
# Week 7: Analyzing Data with Pandas & Visualizing Results with Matplotlib

This project demonstrates **data analysis** and **visualization** using Python’s `pandas`, `matplotlib`, and `seaborn` libraries.  
The **Iris dataset** is used as a sample dataset.

---

## 📊 Features

1. **Data Loading & Exploration**
   - Loads the Iris dataset directly from `seaborn`.
   - Displays dataset structure, missing values, and sample rows.

2. **Data Analysis**
   - Generates descriptive statistics (`.describe()`).
   - Groups data by `species` and calculates mean values of numerical columns.

3. **Visualizations (saved to `/plots`)**
   - **Line Plot**: Trend of petal length across the dataset.
   - **Bar Chart**: Average sepal length per species.
   - **Histogram**: Distribution of petal width.
   - **Scatter Plot**: Relationship between sepal length and petal length, colored by species.

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn

2. Run the script:

```python
python analysis.py
```


3. View generated plots in the plots/ directory.

## 🧩 Observations

Setosa species generally has smaller petal lengths compared to Virginica and Versicolor.

Petal width shows a slightly skewed distribution.

Sepal length correlates positively with petal length.

## ⚡ Tech Stack

pandas – data loading, cleaning, and analysis

matplotlib & seaborn – data visualization

“Data is the new oil, but visualization is the refinery.”


---

### ✨ How to Use
- Save `analysis.py` and `README.md` in a folder (e.g., `Week7_Pandas_Matplotlib`).
- Run the Python script to generate the analysis and save all plots automatically.  
- Open the README for quick documentation of methods, insights, and instructions.
