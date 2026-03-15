Select employee_id 
from Employees 
WHERE salary < 30000
AND manager_id Not In (Select employee_id  from Employees )
AND manager_id IS NOT NULL
order by employee_id

