import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import os
# ============================================================
# Task 2 : Exploratory Data Analysis (EDA)
# ApexPlanet Data Analytics Internship
# Author : Kottakota Gayatri
# ============================================================

# ============================================================
# File Paths
# ============================================================

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataset_path = os.path.join(
    base_path,
    "Dataset",
    "Raw",
    "ApexPlanet_DataAnalytics_Dataset.xlsx"
)
# ============================================================
# Load Dataset
# ============================================================

print("=" * 60)
print("TASK 2 : EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 60)

print("\nLoading Dataset...\n")

df = pd.read_excel(dataset_path)

print("Dataset Loaded Successfully!")
# ============================================================
# Dataset Preview
# ============================================================

print("\n" + "=" * 60)
print("FIRST FIVE ROWS")
print("=" * 60)

print(df.head())
# ============================================================
# Dataset Shape
# ============================================================

print("\n" + "=" * 60)
print("DATASET SHAPE")
print("=" * 60)

print(df.shape)
# ============================================================
# Column Names
# ============================================================

print("\n" + "=" * 60)
print("COLUMN NAMES")
print("=" * 60)

print(df.columns)
# ============================================================
# Dataset Information
# ============================================================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

df.info()
# ============================================================
# Missing Values
# ============================================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())
# ============================================================
# Duplicate Records
# ============================================================

print("\n" + "=" * 60)
print("DUPLICATE RECORDS")
print("=" * 60)

print(df.duplicated().sum())
# ============================================================
# Summary Statistics
# ============================================================

print("\n" + "=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)

print(df.describe())
# ============================================================
# Categorical Summary
# ============================================================

print("\n" + "=" * 60)
print("CATEGORICAL SUMMARY")
print("=" * 60)

print(df.describe(include="object"))
# ============================================================
# Age Distribution Histogram
# ============================================================

print("\nCreating Age Distribution Histogram...")

plt.figure(figsize=(8,5))
sns.histplot(df["Age"], bins=10, kde=True)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    os.path.join(base_path, "Images", "Age_Distribution.png")
)

plt.show()

print("Age Distribution Chart Saved Successfully!")
# ============================================================
# Category-wise Sales Count
# ============================================================

print("\nCreating Category-wise Sales Chart...")

plt.figure(figsize=(8,5))

sns.countplot(
    x="Category",
    data=df,
    order=df["Category"].value_counts().index
)

plt.title("Number of Orders by Category")
plt.xlabel("Category")
plt.ylabel("Number of Orders")
plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(
    os.path.join(base_path, "Images", "Category_Sales_Count.png")
)

plt.show()

print("Category-wise Sales Chart Saved Successfully!")
# ============================================================
# Gender Distribution Pie Chart
# ============================================================

print("\nCreating Gender Distribution Pie Chart...")

gender_counts = df["Gender"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Gender Distribution")

plt.savefig(
    os.path.join(base_path, "Images", "Gender_Distribution.png")
)

plt.show()

print("Gender Distribution Chart Saved Successfully!")
# ============================================================
# Top Cities by Number of Orders
# ============================================================

print("\nCreating Top Cities Chart...")

plt.figure(figsize=(10,5))

sns.countplot(
    y="City",
    data=df,
    order=df["City"].value_counts().index
)

plt.title("Number of Orders by City")
plt.xlabel("Number of Orders")
plt.ylabel("City")

plt.tight_layout()

plt.savefig(
    os.path.join(base_path, "Images", "Top_Cities.png")
)

plt.show()

print("Top Cities Chart Saved Successfully!")
# ============================================================
# Product Distribution
# ============================================================

print("\nCreating Product Distribution Chart...")

plt.figure(figsize=(10,5))

sns.countplot(
    x="Product",
    data=df,
    order=df["Product"].value_counts().index
)

plt.title("Number of Orders by Product")
plt.xlabel("Product")
plt.ylabel("Number of Orders")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    os.path.join(base_path, "Images", "Product_Distribution.png")
)

plt.show()

print("Product Distribution Chart Saved Successfully!")
# ============================================================
# Quantity vs Total Sales (Scatter Plot)
# ============================================================

print("\nCreating Quantity vs Total Sales Scatter Plot...")

plt.figure(figsize=(8,5))

sns.scatterplot(
    x="Quantity",
    y="Total_Sales",
    data=df
)

plt.title("Quantity vs Total Sales")
plt.xlabel("Quantity")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig(
    os.path.join(base_path, "Images", "Quantity_vs_TotalSales.png")
)

plt.show()

print("Quantity vs Total Sales Scatter Plot Saved Successfully!")
# ============================================================
# Correlation Heatmap
# ============================================================

print("\nCreating Correlation Heatmap...")

plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include=["int64", "float64"])

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    os.path.join(base_path, "Images", "Correlation_Heatmap.png")
)

plt.show()

print("Correlation Heatmap Saved Successfully!")
# ============================================================
# Create SQLite Database
# ============================================================

print("\nCreating SQLite Database...")

database_path = os.path.join(
    base_path,
    "SQL",
    "sales_database.db"
)

conn = sqlite3.connect(database_path)

df.to_sql(
    "sales_data",
    conn,
    if_exists="replace",
    index=False
)

print("SQLite Database Created Successfully!")
# ============================================================
# Execute SQL Query 1
# ============================================================

print("\n" + "=" * 60)
print("TOP 5 PRODUCTS BY TOTAL REVENUE")
print("=" * 60)

query = """
SELECT
    Product,
    SUM(Total_Sales) AS Total_Revenue
FROM sales_data
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 5;
"""

result = pd.read_sql_query(query, conn)

print(result)
# ============================================================
# SQL Query 2 : Total Sales by Category
# ============================================================

print("\n" + "=" * 60)
print("TOTAL SALES BY CATEGORY")
print("=" * 60)

query = """
SELECT
    Category,
    SUM(Total_Sales) AS Total_Revenue
FROM sales_data
GROUP BY Category
ORDER BY Total_Revenue DESC;
"""

result = pd.read_sql_query(query, conn)

print(result)
# ============================================================
# SQL Query 3 : Top Cities by Revenue
# ============================================================

print("\n" + "=" * 60)
print("TOP CITIES BY REVENUE")
print("=" * 60)

query = """
SELECT City,
SUM(Total_Sales) AS Revenue
FROM sales_data
GROUP BY City
ORDER BY Revenue DESC;
"""

print(pd.read_sql_query(query, conn))


# ============================================================
# SQL Query 4 : Gender-wise Orders
# ============================================================

print("\n" + "=" * 60)
print("GENDER-WISE ORDERS")
print("=" * 60)

query = """
SELECT Gender,
COUNT(*) AS Orders
FROM sales_data
GROUP BY Gender;
"""

print(pd.read_sql_query(query, conn))


# ============================================================
# SQL Query 5 : Average Customer Age
# ============================================================

print("\n" + "=" * 60)
print("AVERAGE CUSTOMER AGE")
print("=" * 60)

query = """
SELECT ROUND(AVG(Age),2) AS Average_Age
FROM sales_data;
"""

print(pd.read_sql_query(query, conn))


# ============================================================
# SQL Query 6 : Monthly Sales
# ============================================================

print("\n" + "=" * 60)
print("MONTHLY SALES")
print("=" * 60)

query = """
SELECT
substr(Order_Date,6,2) AS Month,
SUM(Total_Sales) AS Revenue
FROM sales_data
GROUP BY Month
ORDER BY Month;
"""

print(pd.read_sql_query(query, conn))


# ============================================================
# SQL Query 7 : Total Orders
# ============================================================

print("\n" + "=" * 60)
print("TOTAL ORDERS")
print("=" * 60)

query = """
SELECT COUNT(*) AS Total_Orders
FROM sales_data;
"""

print(pd.read_sql_query(query, conn))
# Close Database Connection
conn.close()

print("\nSQLite Database Connection Closed Successfully!")