/* Write your T-SQL query statement below */
SELECT 
    P.product_name,
    SUM(O.unit) AS unit 
FROM Orders O
INNER JOIN Products P
    ON P.product_id = O.product_id
WHERE O.order_date like '2020-02-%%'
GROUP BY 
    P.product_id, 
    P.product_name
HAVING SUM(O.unit) >= 100;
