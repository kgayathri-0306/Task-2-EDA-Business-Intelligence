-- ============================================================
-- Task 2 : Business Intelligence SQL Queries
-- ApexPlanet Data Analytics Internship
-- ============================================================

-- Query 1: Top 5 Products by Total Revenue

SELECT
    Product,
    SUM(Total_Sales) AS Total_Revenue
FROM sales_data
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 5;


-- Query 2: Total Sales by Category

SELECT
    Category,
    SUM(Total_Sales) AS Total_Revenue
FROM sales_data
GROUP BY Category
ORDER BY Total_Revenue DESC;


-- Query 3: Top Cities by Revenue

SELECT
    City,
    SUM(Total_Sales) AS Revenue
FROM sales_data
GROUP BY City
ORDER BY Revenue DESC;


-- Query 4: Gender-wise Orders

SELECT
    Gender,
    COUNT(*) AS Orders
FROM sales_data
GROUP BY Gender;


-- Query 5: Average Customer Age

SELECT
    ROUND(AVG(Age), 2) AS Average_Age
FROM sales_data;


-- Query 6: Monthly Sales Trend

SELECT
    substr(Order_Date, 6, 2) AS Month,
    SUM(Total_Sales) AS Revenue
FROM sales_data
GROUP BY Month
ORDER BY Month;


-- Query 7: Total Number of Orders

SELECT
    COUNT(*) AS Total_Orders
FROM sales_data;