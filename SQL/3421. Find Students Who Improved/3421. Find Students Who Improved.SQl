# Write your MySQL query statement below
with score As 
(
    Select student_id , subject,
    FIRST_VALUE(score) OVER (PARTITION BY student_id , subject order by exam_date) AS FValue , 
    FIRST_VALUE (score) OVER (PARTITION BY student_id , subject order by exam_date DESC) AS LValue
    from Scores 
)
select  DISTINCT student_id, subject, FValue AS first_score , LValue AS latest_score from score
where FValue < LValue
order by student_id , subject 