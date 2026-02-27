
[UpVote Please ](https://leetcode.com/problems/monthly-transactions-i/solutions/7613572/stop-fearing-case-when-the-easiest-t-sql-hgok
)
---

# 💡 Intuition

Think of yourself as a bank manager. You have a massive list of transactions. You need to create a monthly report that groups these transactions into folders for each **month** and **country**. For each folder, you need to report the total number of transactions, total money, approved transactions, and approved money.

# 🛠️ Step-by-Step Approach

### Step 1: Grab the Country and Fix the Date 📅

First, we look at our `Transactions` table. The date looks like `2026-02-27 14:30:00`, but we only want `2026-02`.
We use `CONVERT` to turn the date into text, and `SUBSTRING` to chop off everything after the first 7 characters.

```mssql
SELECT 
    SUBSTRING(CONVERT(VARCHAR, trans_date), 1, 7) AS month,
    country
FROM Transactions

```

### Step 2: Organize into Folders (`GROUP BY`) 🗂️🌍

Right now, we just have a giant list. We want to organize this list into separate piles based on the month and country (e.g., a pile for "US in 2026-02").
We do this by adding `GROUP BY` at the very bottom.

```mssql
SELECT 
    SUBSTRING(CONVERT(VARCHAR, trans_date), 1, 7) AS month,
    country
FROM Transactions
GROUP BY 
    SUBSTRING(CONVERT(VARCHAR, trans_date), 1, 7),
    country

```

### Step 3: Count Everything in the Folder 🔢

Now we look inside each folder. How many transactions are in there? We add `COUNT(amount)` to our `SELECT` list to count them.

```mssql
SELECT 
    SUBSTRING(CONVERT(VARCHAR, trans_date), 1, 7) AS month,
    country,
    COUNT(amount) AS trans_count
FROM Transactions
GROUP BY 
    SUBSTRING(CONVERT(VARCHAR, trans_date), 1, 7),
    country

```

### Step 4: Add Up All the Money 💵

Next, we want to know the total dollar amount inside each folder. We add `SUM(amount)` to our `SELECT` list to add up all the money.

```mssql
SELECT 
    SUBSTRING(CONVERT(VARCHAR, trans_date), 1, 7) AS month,
    country,
    COUNT(amount) AS trans_count,
    SUM(amount) AS trans_total_amount
FROM Transactions
GROUP BY 
    SUBSTRING(CONVERT(VARCHAR, trans_date), 1, 7),
    country

```

### Step 5: Count ONLY the Approved Transactions ✅

Here is the tricky part! We only want to count the approved ones. We use `CASE WHEN` to create a tiny rule:
*"If the state is 'approved', count it as a `1`. If it is anything else, count it as a `0`."* Then, we use `SUM()` to add up those `1`s and `0`s.

```mssql
SELECT 
    SUBSTRING(CONVERT(VARCHAR, trans_date), 1, 7) AS month,
    country,
    COUNT(amount) AS trans_count,
    
    SUM(
        CASE
            WHEN state = 'approved' THEN 1
            ELSE 0
        END
    ) AS approved_count,

    SUM(amount) AS trans_total_amount
FROM Transactions
GROUP BY 
    SUBSTRING(CONVERT(VARCHAR, trans_date), 1, 7),
    country

```

### Step 6: Add Up ONLY the Approved Money 💰✅

Finally, we do the same trick for the money.
*"If the state is 'approved', give me the actual `amount` of money. If it is not, give me `$0`."*
Then, we use `SUM()` to add up the money, knowing the declined ones were turned into zero!

```mssql
SELECT 
    SUBSTRING(CONVERT(VARCHAR, trans_date), 1, 7) AS month,
    country,
    COUNT(amount) AS trans_count,
    
    SUM(
        CASE
            WHEN state = 'approved' THEN 1
            ELSE 0
        END
    ) AS approved_count,

    SUM(amount) AS trans_total_amount,
    
    SUM(
        CASE
            WHEN state = 'approved' THEN amount
            ELSE 0
        END
    ) AS approved_total_amount

FROM Transactions
GROUP BY 
    SUBSTRING(CONVERT(VARCHAR, trans_date), 1, 7),
    country

```

# ⏱️ Complexity

* **Time complexity:** $O(N)$
The database reads through all $N$ transactions just once, organizing them into folders and doing the math all at the same time. ⚡
* **Space complexity:** $O(M \times C)$
The database needs enough memory to display one row for every unique combination of Month ($M$) and Country ($C$). 💾

# ✅ Final Code

Here is the complete query from Step 6, ready for you to copy and paste into LeetCode!

```mssql []
/* Write your T-SQL query statement below */
SELECT 
    SUBSTRING(CONVERT(VARCHAR, trans_date), 1, 7) AS month,
    country,
    COUNT(amount) AS trans_count,
    SUM(
        CASE
            WHEN state = 'approved' THEN 1
            ELSE 0
        END
    ) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(
        CASE
            WHEN state = 'approved' THEN amount
            ELSE 0
        END
    ) AS approved_total_amount
FROM Transactions
GROUP BY 
    SUBSTRING(CONVERT(VARCHAR, trans_date), 1, 7),
    country;

```
