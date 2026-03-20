# Write your MySQL query statement below
Select event_day  AS day,emp_id , 
Sum(out_time - in_time ) as total_time
from Employees 
Group by event_day ,emp_id 