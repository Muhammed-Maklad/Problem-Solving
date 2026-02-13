/* Write your T-SQL query statement below */
SELECT
    T.request_at AS [Day],
    ROUND(
        1.0 * SUM(CASE 
                    WHEN T.status IN ('cancelled_by_driver', 'cancelled_by_client') THEN 1 
                    ELSE 0 
                  END) / COUNT(*),
        2
    ) AS [Cancellation Rate]
FROM Trips T
INNER JOIN Users Uc
    ON Uc.users_id = T.client_id
INNER JOIN Users Ud
    ON Ud.users_id = T.driver_id
WHERE Uc.banned = 'No'
  AND Ud.banned = 'No'
  AND T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY T.request_at;
