/* Write your T-SQL query statement below */
SELECT customer_id
From Customer 
Group By customer_id
Having Count (DISTINCT product_key) = (Select Count(*) From Product )