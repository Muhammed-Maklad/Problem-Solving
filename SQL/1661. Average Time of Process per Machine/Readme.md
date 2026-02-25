Here is a step-by-step tutorial breakdown of your solution. This format is perfect for a LeetCode discussion post or personal notes, as it builds the query from the ground up so anyone can understand the logic.

### 🎯 The Goal

We need to find the **average processing time** for each machine.
Processing time for a single process is simply: `end_time - start_time`.

---

### Step 1: The "+ and -" Math Trick

Instead of trying to match the `start` and `end` rows together using complex `JOIN`s, we can use a clever math trick.

If a process starts at timestamp `0.5` and ends at `1.5`, the total time is `1.0`.
Notice that: `1.5 - 0.5 = 1.0` is exactly the same as `(+1.5) + (-0.5) = 1.0`.

Therefore, we can treat all `end` times as **positive** numbers and all `start` times as **negative** numbers. If we add them all up, we get the total processing time!

### Step 2: Apply the Math in SQL (The `CASE` Statement)

We need to tell SQL to make `start` times negative and `end` times positive. We do this using a `CASE` expression:

```sql
CASE
    WHEN activity_type = 'start' THEN -1.00 * timestamp
    ELSE 1.00 * timestamp
END

```

> **Note:** Multiplying by `1.00` ensures our result handles decimals properly and avoids any integer division issues in T-SQL.

### Step 3: Sum it up per Machine

We need to calculate this for each machine, so we will use `GROUP BY machine_id`. Then, we wrap our `CASE` statement in a `SUM()` to get the **total running time** for all processes on that specific machine.

```sql
SELECT machine_id,
       SUM(
           CASE
               WHEN activity_type = 'start' THEN -1.00 * timestamp
               ELSE 1.00 * timestamp
           END
       ) AS total_time
FROM Activity
GROUP BY machine_id

```

### Step 4: Find the Average

We don't just want the total time; we want the *average* time per process. To get this, we divide the total time by the number of unique processes that ran on that machine.

We count the unique processes using `COUNT(DISTINCT process_id)`.

```sql
-- ... SUM(CASE...) / COUNT(DISTINCT process_id) ...

```

### Step 5: Format the Output

The problem requires the final answer to be rounded to 3 decimal places. We wrap our entire math equation in the `ROUND()` function.

```sql
ROUND( (Total_Time / Number_of_Processes), 3 )

```

---

### ✨ The Final Code

Putting all the steps together gives us our final, highly optimized query:

```sql
/* Write your T-SQL query statement below */
SELECT machine_id,
       ROUND(
           SUM(
               CASE
                   WHEN activity_type = 'start' THEN -1.00 * timestamp
                   ELSE 1.00 * timestamp
               END
           ) / COUNT(DISTINCT process_id), 
           3
       ) AS processing_time
FROM Activity
GROUP BY machine_id;

```

### ⏱️ Complexity

* **Time Complexity:** $O(n)$ — We scan the table rows exactly once to aggregate the data.
* **Space Complexity:** $O(m)$ — Where $m$ is the number of distinct machines stored in memory for the `GROUP BY` operation.

---

Would you like me to show you an alternative way to solve this using a `JOIN` (Self-Join) so you can compare the two approaches for your tutorial?