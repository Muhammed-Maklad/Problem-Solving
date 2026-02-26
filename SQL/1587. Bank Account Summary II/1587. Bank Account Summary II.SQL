/* Write your T-SQL query statement below */
SELECT u.name , 
Sum (t.amount) AS balance 
from Users u
Inner join Transactions t
    on t.account = u.account 

group by u.name , u.account 
HAVING Sum (t.amount) > 10000


