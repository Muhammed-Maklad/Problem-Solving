/* Write your T-SQL query statement below */
Select stock_name    , 
SUM 
(
CASE
    When operation ='Buy' Then  -1 * price  
    Else price  
End 
) AS capital_gain_loss 
From Stocks 
group by stock_name    

