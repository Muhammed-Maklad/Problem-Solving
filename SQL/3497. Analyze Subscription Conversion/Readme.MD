
## [UpVote ME](https://leetcode.com/problems/analyze-subscription-conversion/solutions/7693630/step-by-step-how-to-solve-user-activity-8oge9)

### 🧠 The Logical Flow Graphic
![image.png](https://assets.leetcode.com/users/images/f46180e1-2792-4843-96f5-01d0728a04cc_1774468289.594274.png)


### 🚀 The 1-Line Logical Steps


**1️⃣ Open the User's File:** Group all the activities together by `user_id` so we can look at each person's entire timeline as a single block.
```sql
SELECT user_id, 
```

**2️⃣ The Free Trial Bucket:** Sum all the 'free_trial' minutes, divide by the number of 'free_trial' days to find the average, and round it to 2 decimal places.
```sql
    ROUND(
        SUM(CASE WHEN activity_type = 'free_trial' THEN activity_duration ELSE 0 END) * 1.0 /
        COUNT(CASE WHEN activity_type = 'free_trial' THEN 1 END)
    , 2) AS trial_avg_duration, 
```

**3️⃣ The Paid Subscription Bucket:** Do the exact same math, but this time only sum and count the days where the user was 'paid'.
```sql
    ROUND(
        SUM(CASE WHEN activity_type = 'paid' THEN activity_duration ELSE 0 END) * 1.0 /
        COUNT(CASE WHEN activity_type = 'paid' THEN 1 END)
    , 2) AS paid_avg_duration 
FROM UserActivity 
GROUP BY user_id 
```

**4️⃣ The Conversion Filter:** Use `HAVING` to throw away anyone who didn't convert by ensuring they have at least one 'free_trial' day AND at least one 'paid' day.
```sql
HAVING 
    COUNT(CASE WHEN activity_type = 'free_trial' THEN 1 END) > 0 AND
    COUNT(CASE WHEN activity_type = 'paid' THEN 1 END) > 0
```


---

## 💻 The Final Assembled Code

```sql
/* Write your MySQL query statement below */
SELECT user_id, 
    ROUND(
        SUM(CASE WHEN activity_type = 'free_trial' THEN activity_duration ELSE 0 END) * 1.0 /
        COUNT(CASE WHEN activity_type = 'free_trial' THEN 1 END)
    , 2) AS trial_avg_duration, 
    ROUND(
        SUM(CASE WHEN activity_type = 'paid' THEN activity_duration ELSE 0 END) * 1.0 /
        COUNT(CASE WHEN activity_type = 'paid' THEN 1 END)
    , 2) AS paid_avg_duration 
FROM UserActivity 
GROUP BY user_id 
HAVING 
    COUNT(CASE WHEN activity_type = 'free_trial' THEN 1 END) > 0 AND
    COUNT(CASE WHEN activity_type = 'paid' THEN 1 END) > 0
ORDER BY user_id;
```

---

## ⚡ Complexity

* ⏳ **Time Complexity:** O(N) —> We only need to scan the `UserActivity` table exactly once to group the users and calculate their bucket totals.
* 💾 **Space Complexity:** O(M) —> Where M is the number of unique users. The database stores these grouped users in memory to calculate the final averages and apply the `HAVING` filter.

![image.png](https://assets.leetcode.com/users/images/043314ef-6da0-4b16-8320-5032c3023178_1774467961.0327454.png)
