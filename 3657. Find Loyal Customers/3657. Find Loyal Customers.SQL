/* Write your T-SQL query statement below */
SELECT
    customer_id
FROM customer_transactions
GROUP BY customer_id
HAVING
    SUM(CASE WHEN transaction_type = 'purchase' THEN 1 ELSE 0  END) >= 3
    AND
    DATEDIFF(day,MIN(transaction_date), MAX(transaction_date)) >= 30
    AND
    1.0 * SUM(CASE WHEN transaction_type = 'refund' THEN 1 ELSE 0  END)
        / COUNT(transaction_type ) < 0.20
ORDER BY customer_id
