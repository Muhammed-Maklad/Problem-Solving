
/* Write your T-SQL query statement below */
SELECT Department,
       Employee,
       Salary
FROM (
    SELECT D.name AS Department,
           E.name AS Employee,
           E.salary AS Salary,
           DENSE_RANK() OVER (PARTITION BY E.departmentId ORDER BY E.salary DESC) AS RN
    FROM Employee E
    INNER JOIN Department D
        ON D.id = E.departmentId
) t
where Rn <= 3 


