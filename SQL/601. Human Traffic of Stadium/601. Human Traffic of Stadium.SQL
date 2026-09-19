/* Write your T-SQL query statement below */
With FilterGroup AS (
    Select * , id- ROW_NUMBER() over (ORDER BY id) GroupID
    From Stadium 
    Where people >= 100
)
Select id , visit_date  , people 
From FilterGroup
Where GroupID IN(
    Select GroupID From FilterGroup
    Group by GroupID 
    Having count(*) >= 3
)
ORDER BY visit_date ASC