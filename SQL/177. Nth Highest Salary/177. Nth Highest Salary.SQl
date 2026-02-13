CREATE FUNCTION getNthHighestSalary(@N INT)
RETURNS INT
AS
BEGIN
    RETURN (
        SELECT DISTINCT salary
        FROM (
            SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rn
            FROM Employee
        ) t
        WHERE rn = @N
    );
END;
