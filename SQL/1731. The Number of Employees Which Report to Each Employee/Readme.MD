
###  The 1-Line Breakdown

* **1️⃣ The Cloning Machine:** We pretend there are two tables: Table `E` is for the everyday Employees (the workers), and Table `M` is for the Managers (the bosses).
* **2️⃣ The Handshake:** We match them up by making sure the worker's "Boss ID" (`E.reports_to`) perfectly matches the Boss's actual ID badge (`M.employee_id`).
* **3️⃣ The Roll Call:** We use `GROUP BY M.employee_id, M.name` to gather all the workers around their specific boss.
* **4️⃣ Counting Heads:** Now that the teams are grouped together, `COUNT(*)` simply counts how many workers are standing around that manager.
* **5️⃣ Doing the Math:** We take the average age of those specific workers (`AVG(E.age)`) and use `ROUND(..., 0)` to make it a clean, whole number.
* **6️⃣ Line 'Em Up:** Finally, `ORDER BY M.employee_id` sorts the managers neatly by their ID number so HR doesn't get mad!

---

## 💻 The Final SQL Code

```sql
/* Write your MySQL query statement below */
SELECT 
    M.employee_id, 
    M.name, 
    COUNT(*) AS reports_count, 
    ROUND(AVG(E.age), 0) AS average_age 
FROM Employees E
JOIN Employees M 
    ON E.reports_to = M.employee_id 
GROUP BY M.employee_id, M.name 
ORDER BY M.employee_id;
```

---

## ⚡ Complexity
* ⏳ **Time Complexity:** $O(N \log N)$ — The database scans the table to perform the join, and the sorting operation (`ORDER BY`) takes a bit of extra time depending on the number of managers.
* 💾 **Space Complexity:** $O(N)$ — To perform the Self-Join and the `GROUP BY`, the database needs to hold the matching relationships in memory.
