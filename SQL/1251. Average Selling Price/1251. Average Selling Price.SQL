Select P.product_id ,
Round(IFNULL(Sum(units*price) / sum(units), 0) , 2) AS average_price 
from Prices P 
Left Join UnitsSold U
    oN U.product_id = P.product_id
    AND U.purchase_date BETWEEN P.Start_date and P.end_date
Group by  1;
