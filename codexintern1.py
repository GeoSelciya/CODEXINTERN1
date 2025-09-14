import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
file_path = r"C:\Users\GEO\Downloads\data.csv" # <-- replace with your CSV filename
df = pd.read_csv(file_path)

print("=== First 5 Rows of Data ===")
print(df.head())

print("\n=== Data Summary ===")
print(df.describe())

# ---- Basic Analysis ----
# Example: calculate average of a selected column
selected_column = input("\nEnter the column name to calculate average: ")
if selected_column in df.columns:
    avg = df[selected_column].mean()
    print(f"\n✅ Average of '{selected_column}': {avg:.2f}")
else:
    print(f"❌ Column '{selected_column}' not found in dataset!")

# ---- Visualization ----
# 1. Bar Chart (average values of numeric columns)
numeric_means = df.mean(numeric_only=True)
numeric_means.plot(kind="bar", figsize=(8,5), title="Average of Numeric Columns")
plt.xlabel("Columns")
plt.ylabel("Average")
plt.show()

# 2. Scatter Plot (between two numeric columns)
num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
if len(num_cols) >= 2:
    x_col, y_col = num_cols[0], num_cols[1]
    plt.figure(figsize=(6,5))
    plt.scatter(df[x_col], df[y_col], alpha=0.7)
    plt.title(f"Scatter Plot: {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

# 3. Heatmap (correlation matrix)
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ---- Insights Example ----
print("\n=== Insights ===")
print("1. The bar chart shows the average values across numeric columns, useful for quick comparisons.")
print("2. The scatter plot highlights possible relationships between the first two numeric columns.")
print("3. The heatmap reveals correlations: values near +1 indicate strong positive correlation,")
print("   values near -1 indicate strong negative correlation, while values near 0 mean little correlation.")
