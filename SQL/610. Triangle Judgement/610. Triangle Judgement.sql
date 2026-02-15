/* Write your T-SQL query statement below */
Select *,
    CASE 
        WHEN X + Y > Z  AND
            X + Z > Y  AND
            Z + Y > X THEN 'Yes'
        ELSE 'No'

    END  triangle 
FROM Triangle 