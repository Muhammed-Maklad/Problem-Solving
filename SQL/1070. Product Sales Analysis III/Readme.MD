

### 🏃‍♂️ Step 1: Grouping the Racers (`PARTITION BY`)

**The Logic:** Imagine we are hosting a race, but we need separate races for each product.
`PARTITION BY product_id` tells SQL to put all the sales for Product 100 in one group, and all the sales for Product 200 in another group.

```sql
SELECT sale_id, product_id, year, quantity, price, 
       RANK() OVER (PARTITION BY product_id 

```

### ⏱️ Step 2: Finding the Earliest (`ORDER BY`)

**The Logic:** Now that our products are separated into their own races, we need to line them up by time.
`ORDER BY year ASC` sorts the sales from the oldest year to the newest year.

```sql
                    ORDER BY year ASC) AS RK
FROM Sales

```

### 📦 Step 3: The Award Ceremony (The Outer Query)

**The Logic:** Window functions are calculated *after* the `WHERE` clause in SQL, which means we can't filter by our new `RK` column right away.
To fix this, we wrap our entire race inside a subquery (or CTE). Then, the outer query acts as the award ceremony: it only invites the rows where `RK = 1`!

*(💡 **Pro-Tip:** We also use `year AS first_year` here to perfectly match the column name LeetCode expects!)*

```sql
SELECT product_id, year AS first_year, quantity, price
FROM (
    -- Our Race goes inside here!
) t 
WHERE RK = 1;

```

---

## 🧾 The Final SQL Query

When you assemble the inner race and the outer award ceremony, you get this incredibly clean solution:

```sql
/* Write your SQL query statement below */
SELECT product_id, 
       year AS first_year, 
       quantity, 
       price
FROM (
    SELECT sale_id, 
           product_id, 
           year, 
           quantity, 
           price, 
           RANK() OVER (PARTITION BY product_id ORDER BY year ASC) AS RK
    FROM Sales
) t 
WHERE RK = 1;

```

---

## ⚡ Complexity

* **Time Complexity:** $O(N \log N)$ → The database has to sort (`ORDER BY`) the rows within each partition to assign the correct rank.
* **Space Complexity:** $O(N)$ → The window function requires the database to hold the partitions in memory to calculate the rankings.

