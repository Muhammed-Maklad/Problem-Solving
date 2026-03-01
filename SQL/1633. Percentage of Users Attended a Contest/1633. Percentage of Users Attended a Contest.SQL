# Write your MySQL query statement below
Select Distinct contest_id ,
ROUND(count(user_id)/
    (select count(distinct user_id) from Users)*100,2) as percentage 

from Register 
group by 1
order by 2 desc, 1