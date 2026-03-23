WITH user_counts AS (
    SELECT u.name, COUNT(*) AS cnt
    FROM Users u
    JOIN MovieRating mr ON u.user_id = mr.user_id
    GROUP BY u.user_id
),
movie_avg AS (
    SELECT m.title, AVG(mr.rating) AS avg_rating
    FROM Movies m
    JOIN MovieRating mr ON m.movie_id = mr.movie_id
    WHERE mr.created_at >= '2020-02-01'
      AND mr.created_at < '2020-03-01'
    GROUP BY m.movie_id
)

(
    SELECT name AS results
    FROM user_counts
    ORDER BY cnt DESC, name
    LIMIT 1
)

UNION ALL

(
    SELECT title AS results
    FROM movie_avg
    ORDER BY avg_rating DESC, title
    LIMIT 1
);

