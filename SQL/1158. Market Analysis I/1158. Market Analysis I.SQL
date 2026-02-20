/* Write your T-SQL query statement below */
Select  U.user_id  AS buyer_id ,
join_date  , 
ISNULL(Count(order_id),0) AS orders_in_2019 
From Users U
Left Join Orders O
    ON U.user_id  = O.buyer_id 
    And Year(order_date) = '2019'
Group BY  U.user_id , join_date
