# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------
try:
    df = pd.read_csv("sales.csv")
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ File not found! Please check the file path.")
    df = pd.DataFrame()  # create empty frame so script doesn't crash

# If dataset is loaded
if not df.empty:
    print("Preview of dataset:")
    print(df.head(), "\n")

    print("Dataset Info:")
    print(df.info(), "\n")

    print("Missing Values:")
    print(df.isnull().sum(), "\n")

    # Clean missing values (drop or fill)
    df = df.dropna()

    # -------------------------------
    # Task 2: Basic Data Analysis
    # -------------------------------
    print("Descriptive Statistics:")
    print(df.describe(), "\n")

    # Grouping by region
    avg_sales_region = df.groupby("region")["sales"].mean()
    print("Average Sales per Region:")
    print(avg_sales_region, "\n")

    # Grouping by product
    avg_sales_product = df.groupby("product")["sales"].mean()
    print("Average Sales per Product:")
    print(avg_sales_product, "\n")

    # -------------------------------
    # Task 3: Data Visualization
    # -------------------------------

    sns.set_style("whitegrid")  # use seaborn theme

    # 1. Line chart - Sales over time
    plt.figure(figsize=(8,5))
    sns.lineplot(data=df, x="date", y="sales", marker="o", label="Sales")
    plt.title("Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales Amount")
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

    # 2. Bar chart - Average sales by region
    plt.figure(figsize=(6,4))
    sns.barplot(x=avg_sales_region.index, y=avg_sales_region.values, palette="Blues_d")
    plt.title("Average Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Average Sales")
    plt.show()

    # 3. Histogram - Sales distribution
    plt.figure(figsize=(6,4))
    sns.histplot(df["sales"], bins=6, kde=True, color="purple")
    plt.title("Distribution of Sales")
    plt.xlabel("Sales Amount")
    plt.ylabel("Frequency")
    plt.show()

    # 4. Scatter plot - Sales vs index
    plt.figure(figsize=(6,4))
    sns.scatterplot(x=df.index, y="sales", hue="region", style="product", s=100, data=df)
    plt.title("Scatter Plot of Sales by Region and Product")
    plt.xlabel("Transaction Index")
    plt.ylabel("Sales Amount")
    plt.legend(title="Region / Product")
    plt.show()

    # -------------------------------
    # Task 4: Observations & Findings
    # -------------------------------
    print("📊 Findings & Insights:")
    print("- Sales have fluctuating trends over time, with noticeable peaks in some months.")
    print("- The region with the highest average sales is likely 'Kenya' (check bar chart).")
    print("- Sales distribution shows a concentration around mid-range values, with fewer very high sales.")
    print("- The scatter plot indicates variation by both region and product, suggesting product performance differs across regions.")