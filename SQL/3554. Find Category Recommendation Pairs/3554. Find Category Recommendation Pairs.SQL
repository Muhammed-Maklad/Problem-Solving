# Write your MySQL query statement below
With UserCategories As (
    Select 
        DISTINCT PPU.user_id  , Pinfo.category
    From ProductPurchases PPU , ProductInfo Pinfo 
    Where Pinfo.product_id  = PPU.product_id 
),
Pairs As (
    Select 
            A.user_id , A.category As category1   ,
            B.category As category2 
        From UserCategories A , UserCategories B
        Where A.user_id = B.user_id 
            AND A.category < B.category
)

Select
    category1 , category2 ,
    Count(DISTINCT user_id) As customer_count 
From Pairs 
Group By  category1 , category2
    HAVING customer_count >= 3
Order By 3 DESC , 1 ASC,2 ASC