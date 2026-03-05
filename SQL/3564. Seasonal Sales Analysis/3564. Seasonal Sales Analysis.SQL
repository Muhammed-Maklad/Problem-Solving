select season, category, total_quantity, total_revenue
from (
    SELECT
        CASE
            WHEN MONTH(sale_date) IN (12, 1, 2) THEN 'Winter'
            WHEN MONTH(sale_date) IN (3, 4, 5) THEN 'Spring'
            WHEN MONTH(sale_date) IN (6, 7, 8) THEN 'Summer'
            WHEN MONTH(sale_date) IN (9, 10, 11) THEN 'Fall'
        END AS season,
        p.category,
            SUM(quantity ) AS total_quantity ,
            SUM(quantity * price) AS total_revenue  
            from sales s 
            Inner join products p
                ON p.product_id  = s.product_id 
                group by season, category
    order by total_quantity desc, total_revenue desc
) t
group by season
order by season;


