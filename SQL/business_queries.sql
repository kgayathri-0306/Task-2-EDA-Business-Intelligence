-- Question 1
-- What are the Top 5 Products by Total Revenue?

SELECT
    Product,
    SUM(Total_Sales) AS Total_Revenue
FROM sales_data
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 5;