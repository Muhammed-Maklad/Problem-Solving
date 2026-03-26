# Write your MySQL query statement below
Select S.employee_id 
from Salaries S
Left Join Employees E
    On S.employee_id = E.employee_id
where E.employee_id Is Null

Union All

Select E.employee_id 
from Employees E
Left Join Salaries S
    On S.employee_id = E.employee_id
where S.employee_id Is Null

ORDER BY employee_id


