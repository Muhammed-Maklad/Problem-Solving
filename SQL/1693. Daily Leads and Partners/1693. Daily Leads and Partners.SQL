# Write your MySQL query statement below
Select date_id  , make_name , 
    Count(DISTINCT lead_id) AS unique_leads ,
    Count(DISTINCT partner_id) AS unique_partners
from DailySales
Group by date_id  , make_name;
