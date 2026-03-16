Select product_id, year AS first_year, quantity, price
from 
(
    Select sale_id ,product_id , year , quantity  , price , 
           RANK() OVER (partition By product_id  ORDER BY year ASC) AS RK
    From Sales
)t 
WHERE RK = 1;