## [UpVote me ](./https://leetcode.com/problems/find-consistently-improving-employees/solutions/7714792/simple-solution-step-by-step-with-100-be-8no0)

![image.png](https://assets.leetcode.com/users/images/d8661587-550f-40fc-9ffb-2034c8d86747_1774796908.882347.png)

### Logical Graphic Think

![image.png](https://assets.leetcode.com/users/images/8d9df77f-ccc3-477e-9ec5-26a84deb7b68_1774797373.2548554.png)

###  The Logical Steps
**1️⃣ Number the Report Cards:** We stick a number on every review starting with the newest one (`1`), then the second newest (`2`), and so on.
```sql
WITH RankedReviews AS (
    SELECT pr.employee_id, pr.review_date, e.name, pr.rating,
           ROW_NUMBER() OVER (PARTITION BY pr.employee_id ORDER BY pr.review_date DESC) AS rn
    FROM performance_reviews pr
    JOIN employees e
        ON e.employee_id = pr.employee_id
),
```

**2️⃣ Keep Only the Top 3:** We throw away all the old history and only keep the report cards labeled 1, 2, or 3.
```sql
Last3 AS (
    SELECT *
    FROM RankedReviews
    WHERE rn <= 3
),
```

**3️⃣ Lay Them Side-by-Side:** We use `LAG()` to grab the "Middle" grade (`prev`) and the "Oldest" grade (`prev2`) and slide them onto the exact same row as the "Newest" grade so we can compare them instantly.
```sql
Increase AS (
    SELECT *,
           LAG(rating, 1) OVER (PARTITION BY employee_id ORDER BY review_date) AS prev,
           LAG(rating, 2) OVER (PARTITION BY employee_id ORDER BY review_date) AS prev2
    FROM Last3
)
```

**4️⃣ Check the Grades:** We filter the list to make sure they actually have 3 report cards (`prev2 IS NOT NULL`), check that Newest > Middle and Middle > Oldest, and subtract the oldest from the newest to get the final score.
```sql
SELECT employee_id, name, rating - prev2 AS improvement_score
FROM Increase
WHERE prev2 IS NOT NULL
  AND rating > prev
  AND prev > prev2
```

**5️⃣ Sort the Winners:** We put the most improved employees at the very top of the list!
```sql
ORDER BY improvement_score DESC, name;
```

---

## 💻 The Final Assembled Code

```sql
/* Write your MySQL query statement below */
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
Increase AS (
    SELECT *,
           LAG(rating, 1) OVER (PARTITION BY employee_id ORDER BY review_date) AS prev,
           LAG(rating, 2) OVER (PARTITION BY employee_id ORDER BY review_date) AS prev2
    FROM Last3
)

SELECT employee_id, name, rating - prev2 AS improvement_score
FROM Increase
WHERE prev2 IS NOT NULL
  AND rating > prev
  AND prev > prev2
ORDER BY improvement_score DESC, name;
```

---

## ⚡ Complexity

* ⏳ **Time Complexity:** $O(N \log N)$ —> Sorting the data to number the reviews (`ROW_NUMBER`) and lay them side-by-side (`LAG`) takes a bit of computing power.
* 💾 **Space Complexity:** $O(N)$ —> The database has to hold the narrowed-down list of top 3 reviews in its memory to do the final math.

---

![image.png](https://assets.leetcode.com/users/images/2cfc967f-003d-4731-9931-ff9e3ca6fdf5_1774797216.7248363.png)
