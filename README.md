📊 CSV Data Analysis Tool

A Python-based tool that uses Pandas, Matplotlib, and Seaborn to load a CSV file, perform basic data analysis, and generate visualizations.

🚀 Features

Load and preview a CSV dataset

Calculate statistics (e.g., average of a column)

Generate visualizations:

📊 Bar Chart (average values of numeric columns)

🔵 Scatter Plot (relationship between two numeric columns)

🌡️ Heatmap (correlation between numeric columns)

Print insights and observations

📂 Project Structure
codexintern1.py     # Main Python script
data.csv            # Sample dataset
README.md           # Documentation

⚙️ Requirements

Python 3.8+

Pandas

Matplotlib

Seaborn

Install dependencies with:

pip install pandas matplotlib seaborn

▶️ How to Run

Place your dataset (e.g., data.csv) in the project folder.

Open the terminal in VS Code.

Run the script:

python codexintern1.py

📝 Example Usage

Menu flow:

The script loads your CSV.

You enter the column name to calculate its average.

Visualizations appear one by one (bar chart, scatter plot, heatmap).

Insights are displayed in the terminal.

📊 Sample Dataset (data.csv)
Product	Category	Sales	Profit	Advertising_Spend
Laptop	Electronics	1200	300	200
Tablet	Electronics	800	150	150
Phone	Electronics	600	200	180
Monitor	Electronics	300	50	100
Headphones	Accessories	150	30	50
📌 Insights Example

The bar chart shows the average of numeric columns (Sales, Profit, Advertising_Spend).

The scatter plot reveals relationships (e.g., higher Sales often mean higher Profit).

The heatmap highlights correlations (Advertising_Spend is strongly correlated with Sales).

🏆 Author

Developed as a Python project for practicing data analysis and visualization.
