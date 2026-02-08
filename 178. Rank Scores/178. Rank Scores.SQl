/* Write your T-SQL query statement below */
Select score ,
    Dense_rank () over (Order by Score DESC ) Rank
From Scores 
order by Rank
