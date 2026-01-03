-- Total revenue
SELECT SUM(sales) AS total_revenue
FROM clean_retail_sales;

-- Revenue by category
SELECT category, SUM(sales) AS revenue
FROM clean_retail_sales
GROUP BY category
ORDER BY revenue DESC;

-- Daily sales trend
SELECT order_date, SUM(sales) AS daily_sales
FROM clean_retail_sales
GROUP BY order_date
ORDER BY order_date;
