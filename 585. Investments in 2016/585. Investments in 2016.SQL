# Write your MySQL query statement below
Select ROUND(Sum(tiv_2016 ),2) As tiv_2016 
From Insurance 
Where tiv_2015 IN 
(
    Select tiv_2015 
    from Insurance
    Group By tiv_2015
    Having Count(*) > 1
) AND
(lat,Lon) IN 
(
    Select lat,Lon 
    from Insurance
    Group By lat,Lon 
    Having Count(*) = 1
) 