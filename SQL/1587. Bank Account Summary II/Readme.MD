
# 💡 Intuition

Imagine we have two lists: one with people's names 🧍‍♂️ and one with their bank receipts 🧾. We just need to match the receipts to the right person 🔗, add up their money 💰, and only keep the VIPs who have more than 10,000 👑.

# 🛠️ Approach

Let's build the code one simple step at a time:

### Step 1: Link the tables together 🔗

First, we need to bring the `Users` table and `Transactions` table together. We use an `INNER JOIN` to connect them wherever their `account` numbers match.

```mssql
FROM Users u
INNER JOIN Transactions t
    ON t.account = u.account

```

### Step 2: Group the receipts by person 📦

Right now, if a user bought 5 things, they show up 5 times. We use `GROUP BY` to organize the data into one neat box per person.

```mssql
FROM Users u
INNER JOIN Transactions t
    ON t.account = u.account
GROUP BY u.name, u.account

```

### Step 3: Add up the total money ➕💰

Now that everyone's receipts are in their own box, we do the math! We use `SELECT` to show the user's name, and `SUM(t.amount)` to add up all their money. We will call this total their `balance`.

```mssql
SELECT u.name, SUM(t.amount) AS balance
FROM Users u
INNER JOIN Transactions t
    ON t.account = u.account
GROUP BY u.name, u.account

```

### Step 4: Keep only the VIPs 🛑

Finally, we only want to show users with a balance over 10,000. Because we are filtering a *total sum* that we just calculated, SQL rules say we must use the word `HAVING` instead of `WHERE`.

```mssql
SELECT u.name, SUM(t.amount) AS balance
FROM Users u
INNER JOIN Transactions t
    ON t.account = u.account
GROUP BY u.name, u.account
HAVING SUM(t.amount) > 10000

```

# ⏱️ Complexity

* **Time complexity:** $O(N)$
The computer quickly reads through the lists once to match the accounts and do the math. ⚡
* **Space complexity:** $O(N)$
The computer uses a tiny bit of memory to hold the grouped totals before showing us the answer. 💾

# ✅ Final Code

Here is the complete code ready to copy and paste:

```mssql []
/* Write your T-SQL query statement below */
SELECT 
    u.name, 
    SUM(t.amount) AS balance 
FROM Users u
INNER JOIN Transactions t
    ON t.account = u.account 
GROUP BY 
    u.name, 
    u.account 
HAVING 
    SUM(t.amount) > 10000;

```

---

Would you like me to explain the exact difference between `WHERE` and `HAVING` with a super quick example?

![UPvote](https://i.imgflip.com/57jfh9.jpg)