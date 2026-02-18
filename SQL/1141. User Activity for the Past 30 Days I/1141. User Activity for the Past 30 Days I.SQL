/* Write your T-SQL query statement below */
Select activity_date AS day ,
count (DISTINCT user_id ) AS active_users 
From Activity 
Where activity_date BETWEEN '2019-06-28' AND '2019-07-27'

Group by activity_date

