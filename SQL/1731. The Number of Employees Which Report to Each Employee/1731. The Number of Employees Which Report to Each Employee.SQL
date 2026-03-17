# Write your MySQL query statement below
Select M.employee_id  , M.name , Count(*) As reports_count , 
Round(AVG(E.age),0) AS average_age 
from Employees E
Join Employees M 
    ON E.reports_to =  M.employee_id 
group by M.employee_id  , M.name 
order by M.employee_id

