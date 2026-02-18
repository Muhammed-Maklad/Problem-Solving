/* Write your T-SQL query statement below */
Select project_id  ,
ROUND(AVG(1.00*E.experience_years),2) AS average_years 
From Project P
Left join Employee E
    on P.employee_id = E.employee_id  
group by P.project_id  
