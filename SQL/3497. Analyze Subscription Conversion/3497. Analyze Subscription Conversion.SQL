# Write your MySQL query statement below
Select user_id , 
    ROUND(
        SUM(CASE WHEN activity_type = 'free_trial' Then activity_duration ELSE 0 END)* 1.0  /
        COUNT(CASE WHEN activity_type = 'free_trial' Then 1  END)
        ,2) AS trial_avg_duration  , 
    ROUND(
        SUM(CASE WHEN activity_type = 'paid' Then activity_duration ELSE 0 END)* 1.0  /
        COUNT(CASE WHEN activity_type = 'paid' Then 1 END)
        ,2) AS paid_avg_duration 
From UserActivity 
Group by user_id 
HAVING 
    COUNT(CASE WHEN activity_type = 'free_trial' THEN 1 END) > 0 AND
    COUNT(CASE WHEN activity_type = 'paid' THEN 1 END) > 0
order by user_id 

