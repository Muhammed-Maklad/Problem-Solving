Select user_id , MAX(time_stamp)  As last_stamp
from Logins 
Where YEAR(time_stamp) = '2020'
GROUP BY user_id;