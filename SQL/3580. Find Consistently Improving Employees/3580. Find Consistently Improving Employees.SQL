WITH RankedReviews AS (
    SELECT pr.employee_id, pr.review_date, e.name, pr.rating,
           ROW_NUMBER() OVER (PARTITION BY pr.employee_id ORDER BY pr.review_date DESC) AS rn
    FROM performance_reviews pr
    JOIN employees e
        ON e.employee_id = pr.employee_id
),
Last3 AS (
    SELECT *
    FROM RankedReviews
    WHERE rn <= 3
),
Increse AS (
    SELECT *,
           LAG(rating, 1) OVER (PARTITION BY employee_id ORDER BY review_date) AS prev,
           LAG(rating, 2) OVER (PARTITION BY employee_id ORDER BY review_date) AS prev2
    FROM Last3
)
SELECT employee_id, name, rating - prev2 AS improvement_score
FROM Increse
WHERE prev2 IS NOT NULL
  AND rating > prev
  AND prev > prev2
ORDER BY improvement_score DESC, name;

