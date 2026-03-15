Select user_id , Count(follower_id) AS followers_count 
from Followers 
Group by user_id 
order by user_id  ;