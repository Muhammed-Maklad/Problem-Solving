/* Write your T-SQL query statement below */
Select employee_id ,
Case 
    When substring(name,1,1) <>'M' and employee_id % 2 <> 0 then salary
    Else  0
End AS bonus 
from Employees 
order by employee_id;

