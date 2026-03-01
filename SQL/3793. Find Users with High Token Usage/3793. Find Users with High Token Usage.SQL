# Write your MySQL query statement below
Select user_id ,
Count(prompt) AS prompt_count , 
Round(AVG(tokens),2) As avg_tokens 
From prompts 
group by user_id
Having  Count(prompt)  >= 3
    AND MAX(tokens) > AVG(tokens)
ORDER BY avg_tokens DESC, user_id;