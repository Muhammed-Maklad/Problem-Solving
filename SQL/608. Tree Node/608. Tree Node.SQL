/* Write your T-SQL query statement below */
Select id ,
CASE
    When p_id is NULL Then 'Root'
    When id in (Select p_id From Tree Where p_id IS Not Null) Then 'Inner'
    Else 'Leaf'
END AS type
From Tree