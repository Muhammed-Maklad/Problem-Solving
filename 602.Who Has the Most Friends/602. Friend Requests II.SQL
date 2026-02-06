# Write your MySQL query statement below

Select requester_id AS id ,
Count(*) AS num 
From (
    Select requester_id From RequestAccepted 
    union ALL
    Select accepter_id  From RequestAccepted 
) As RequestAccepted 
Group By id
ORDER BY num DESC
limit 1;