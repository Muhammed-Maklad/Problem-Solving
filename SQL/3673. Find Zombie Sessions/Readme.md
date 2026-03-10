## 🧟‍♂️ **How to Detect “Zombie Sessions” in SQL (Simple 6-Step Guide)**


# [UPVOTE](https://leetcode.com/problems/find-zombie-sessions/solutions/7637982/stop-writing-messy-sql-the-6-step-zombie-6sze)
---

## 1️⃣ Group Events by Session

First, group all events by **`session_id`** and **`user_id`**.
This lets us analyze the **whole session timeline** instead of individual events.

```sql
SELECT 
    session_id,
    user_id
```

---

## 2️⃣ Calculate Session Duration

Find how long the session lasted by calculating the difference between USING `TIMESTAMPDIFF`:

* **First event** → `MIN(event_timestamp)`
* **Last event** → `MAX(event_timestamp)`

```sql
TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) 
AS session_duration_minutes
```

---

## 3️⃣ Count Scroll Events

Count how many times the user **scrolled** in the session.

We use `CASE WHEN`:

* Add **1** if the event is `scroll`
* Add **0** otherwise

```sql
SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) AS scroll_count
```

---

## 4️⃣ Filter Long and Scroll-Heavy Sessions

Use `HAVING` to filter sessions that:

* Last **more than 30 minutes**
* Have **at least 5 scrolls**

```sql
HAVING 
    TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) > 30
    AND SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) >= 5
```

---

## 5️⃣ Check Click-to-Scroll Ratio

Zombie sessions rarely click.

We calculate:

```
clicks / scrolls
```

If the ratio is **less than 0.20**, it means very few clicks.

```sql
AND SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) * 1.0 /
    SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) < 0.20
```


---

## 6️⃣ Ensure No Purchases

Zombie users **never buy anything**, so the number of `purchase` events must be **0**.

```sql
AND SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) = 0
```
---
## ⚡ Complexity

* **Time Complexity:** `O(N)` → Scan the events table once.
* **Space Complexity:** `O(M)` → Store grouped sessions in memory.

---

## 🧾 Final SQL Query

```sql
SELECT 
    session_id,
    user_id,
    TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) AS session_duration_minutes,
    SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) AS scroll_count
FROM app_events
GROUP BY session_id, user_id
HAVING 
    TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) > 30
    AND SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) >= 5
    AND SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) * 1.0 /
        SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END) < 0.20
    AND SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) = 0
ORDER BY scroll_count DESC, session_id ASC;
```

---
![image.png](https://assets.leetcode.com/users/images/6e014042-e139-4350-b803-c5708cdc42c9_1772931949.5822384.png)

