SELECT 
    ROUND(
        COUNT(DISTINCT player.player_id) * 1.0 /
        (SELECT COUNT(DISTINCT player_id) FROM Activity),
    2) AS fraction
FROM
(
    SELECT player_id, MIN(event_date) AS event_date
    FROM Activity
    GROUP BY player_id
) player
INNER JOIN Activity A
    ON A.player_id = player.player_id
WHERE DATEDIFF(A.event_date, player.event_date) = 1;

