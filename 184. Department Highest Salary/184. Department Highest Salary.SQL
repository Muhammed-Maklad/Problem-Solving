SELECT
    Department,
    Employee,
    Salary
FROM (
    SELECT
        D.name AS Department,
        E.name AS Employee,
        E.Salary,
        DENSE_RANK() OVER (
            PARTITION BY E.departmentId
            ORDER BY E.Salary DESC
        ) AS RS
    FROM Employee E
    INNER JOIN Department D
        ON D.id = E.departmentId
) t
WHERE RS = 1
ORDER BY Salary DESC;
