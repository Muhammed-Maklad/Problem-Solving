# Write your MySQL query statement below
SELECT 'Low Salary' AS category , 
    Count(IF(income < 20000 , 1 , NULL)) AS accounts_count
    From Accounts 
UNION ALL

SELECT 'Average Salary' AS category , 
    Count(IF(income >= 20000 and income <= 50000, 1 , NULL)) AS accounts_count
    From Accounts 
UNION ALL

SELECT 'High Salary' AS category , 
    Count(IF(income > 50000 , 1 , NULL)) AS accounts_count
    From Accounts 


