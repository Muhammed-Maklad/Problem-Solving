# Write your MySQL query statement below
SELECT W.id
FROM Weather W
JOIN Weather We
    ON DATEDIFF(W.recordDate, We.recordDate) = 1
WHERE W.temperature > We.temperature

