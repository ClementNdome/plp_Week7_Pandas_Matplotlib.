import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- SETUP --------------------
# Create plots directory if not exists
os.makedirs("plots", exist_ok=True)

print("=== Week 7: Pandas + Matplotlib Analysis ===")

# -------------------- LOAD DATA --------------------
try:
    # Load Iris dataset from seaborn
    df = sns.load_dataset("iris")
    print("\n✅ Dataset loaded successfully!")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")
    exit()

# Inspect the first few rows
print("\n--- First 5 Rows ---")
print(df.head())

# Check info and missing values
print("\n--- Dataset Info ---")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# -------------------- BASIC ANALYSIS --------------------
# Summary statistics
print("\n--- Descriptive Statistics ---")
print(df.describe())

# Group by species to compute mean of numeric columns
group_means = df.groupby("species").mean(numeric_only=True)
print("\n--- Mean Values by Species ---")
print(group_means)

# -------------------- VISUALIZATIONS --------------------
sns.set_theme(style="whitegrid")

# 1️⃣ Line Chart – Trend of petal_length across rows
plt.figure(figsize=(8,4))
plt.plot(df.index, df["petal_length"], color="purple")
plt.title("Petal Length Trend (Index Order)")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.savefig("plots/line_plot.png")
plt.close()

# 2️⃣ Bar Chart – Average sepal_length by species
plt.figure(figsize=(6,4))
group_means["sepal_length"].plot(kind="bar", color=["#FF9999","#66B2FF","#99FF99"])
plt.title("Average Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.tight_layout()
plt.savefig("plots/bar_chart.png")
plt.close()

# 3️⃣ Histogram – Distribution of petal_width
plt.figure(figsize=(6,4))
plt.hist(df["petal_width"], bins=20, color="orange", edgecolor="black")
plt.title("Distribution of Petal Width")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("plots/histogram.png")
plt.close()

# 4️⃣ Scatter Plot – Sepal Length vs. Petal Length
plt.figure(figsize=(6,5))
sns.scatterplot(data=df, x="sepal_length", y="petal_length", hue="species", palette="Set1")
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.savefig("plots/scatter_plot.png")
plt.close()

print("\n✅ Plots saved inside the 'plots/' directory.")
print("\nAnalysis Complete!")
