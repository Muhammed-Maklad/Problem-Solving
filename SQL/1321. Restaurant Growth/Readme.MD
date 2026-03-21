 
## [UPVote Me](https://leetcode.com/problems/restaurant-growth/solutions/7678096/from-zero-to-hero-master-7-day-rolling-s-5sav)
### 🧠 The Logical Flow Graphic


**Aggregate daily amounts, then calculate a 7-day moving sum and average using a window function.**


![image.png](https://assets.leetcode.com/users/images/53e6410c-e40a-467f-9d4d-21d05bf83620_1774105459.3822505.png)


**1️⃣ Squash the Days:** Group the data by date to merge all individual customer receipts into one total sum for each day.
```sql
WITH daily AS (
    SELECT 
        visited_on,
        SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
),
```

**2️⃣ The Conveyor Belt Window:** Sort the days chronologically and scoop up today's money plus the previous 6 days into a rolling 7-day sum.
```sql
Sum7D AS (
    SELECT 
        visited_on,
        SUM(daily_amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amountSum, 
```

**3️⃣ Count the Days:** Assign a row number to each date so we can track exactly how many days the restaurant has been open.
```sql
        ROW_NUMBER() OVER (ORDER BY visited_on) AS Week 
    FROM daily
)
```

**4️⃣ Find the Average:** Select the date, grab the 7-day total, and divide it by 7.0 (rounded to two decimal places) to find the daily average.
```sql
SELECT 
    visited_on,
    amountSum AS amount,
    ROUND(amountSum / 7.0, 2) AS average_amount
FROM Sum7D
```

**5️⃣ The Filter:** Throw away the first 6 days because they don't have enough history to make a complete 7-day window.
```sql
WHERE Week >= 7
```

**6️⃣ Line Them Up:** Sort the final output so the report flows perfectly chronologically from oldest to newest.
```sql
ORDER BY visited_on;
```



---

## 💻 The Final Assembled Code

```sql
/* Write your MySQL query statement below */
WITH daily AS (
    SELECT 
        visited_on,
        SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
),
Sum7D AS (
    SELECT 
        visited_on,
        SUM(daily_amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amountSum, 
        ROW_NUMBER() OVER (ORDER BY visited_on) AS Week 
    FROM daily
)

SELECT 
    visited_on,
    amountSum AS amount,
    ROUND(amountSum / 7.0, 2) AS average_amount
FROM Sum7D
WHERE Week >= 7
ORDER BY visited_on;
```

---

## ⚡ Complexity

* ⏳ **Time Complexity:** O(N log N) —> The database engine must sort the dates to properly execute both the window functions (`OVER ORDER BY`) and the final `ORDER BY` clause.
* 💾 **Space Complexity:** O(N) —> We create temporary Common Table Expressions (`daily` and `Sum7D`) which the database stores in memory to calculate the final 7-day windows.

![image.png](https://assets.leetcode.com/users/images/ce163e75-e7ff-41af-a2b7-d1eb962e7d80_1774105723.833566.png)

