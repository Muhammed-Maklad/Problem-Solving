# Write your MySQL query statement below
Select S.student_id  , S.student_name , SU.subject_name ,
Count(E.student_id) AS attended_exams
From Students S
Join Subjects SU

LEFT  Join Examinations E 
   ON S.student_id = E.student_id
    AND SU.subject_name = E.subject_name
 

group by S.student_id  , S.student_name , SU.subject_name 
order by S.student_id  , S.student_name , SU.subject_name 