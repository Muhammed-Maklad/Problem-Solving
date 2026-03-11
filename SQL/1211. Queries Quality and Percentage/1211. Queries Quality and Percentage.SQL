Select query_name ,
    Round(AVG(rating  / position ) , 2) AS quality ,
    round((count(case when rating<3 then rating end)/count(rating))*100,2) AS poor_query_percentage 
from Queries 
group by query_name

