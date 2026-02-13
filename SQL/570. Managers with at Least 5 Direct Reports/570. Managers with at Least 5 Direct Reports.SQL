/* Write your T-SQL query statement below */
Select name 
From 
Employee 
Where id  IN (
    SELECT managerId
    from Employee E
    Group By managerId 
    HAVING Count(*) > 4 
)
