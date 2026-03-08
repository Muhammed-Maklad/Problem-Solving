
## [UpVote Please][https://leetcode.com/problems/exchange-seats/solutions/7633406/sql-musical-chairs-the-swapping-seats-tr-075c]

Here is a visual of how the teacher moves the seat numbers around:

```text
 🪑 Odd Seats move RIGHT (+1)      🪑 Even Seats move LEFT (-1)
       [1] -----> [2]                    [1] <----- [2]
      Abbot       Doris                 Abbot       Doris

 🪑 The Last Odd Seat? (No partner, stays the same!)
       [5]
      Jeames

```

Let's break down the teacher's rules step-by-step!

---

### 1. 🚶‍♂️ The Odd Seats Move Forward (`id % 2 = 1`)

* **The Joke:** If you are sitting in an odd-numbered seat (1, 3, 5), the teacher tells you to move one seat forward (`id + 1`).
```sql
SELECT 
    CASE
        WHEN id % 2 = 1 AND id + 1 <= (SELECT MAX(id) FROM Seat) THEN id + 1

```

### 2. 🚶‍♀️ The Even Seats Move Backward (`id % 2 = 0`)

* **The Joke:** If you are sitting in an even-numbered seat (2, 4, 6), you have it easy. You subtract 1 from your seat number (`id - 1`).

```sql
        WHEN id % 2 = 0 THEN id - 1

```

### 3. 🧍‍♂️ The Lonely Last Student (`ELSE`)

* If neither of the above rules applied, the ID stays exactly the same.

```sql
        ELSE id
    END AS id,
    student

```

### ⏱️ Complexity

* ⏳ **Time Complexity:** $O(N^2)$ in some databases because of the `(SELECT MAX(id) FROM Seat)` running on every row, but in modern optimized SQL engines, it is cached and runs closer to $O(N)$. We check each student once.
* 💾 **Space Complexity:** $O(1)$ — We don't create any new tables, just output the results!

---

## 💻 The Final Assembled Code


```sql
/* Write your SQL query statement below */
SELECT 
    CASE
        WHEN id % 2 = 1 AND id + 1 <= (SELECT MAX(id) FROM Seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;

```

![image.png](https://assets.leetcode.com/users/images/6e014042-e139-4350-b803-c5708cdc42c9_1772931949.5822384.png)



[https://leetcode.com/problems/exchange-seats/solutions/7633406/sql-musical-chairs-the-swapping-seats-tr-075c]: https://leetcode.com/problems/exchange-seats/solutions/7633406/sql-musical-chairs-the-swapping-seats-tr-075c