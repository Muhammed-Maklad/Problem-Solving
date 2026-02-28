# 🛑 Regex: The VIP Club Bouncer (Super Simple Edition)

# [UpVote ME ](https://leetcode.com/problems/find-valid-emails/solutions/7615975/never-fail-an-email-regex-again-the-5-st-tih7)

### 1. The `^` and `$`

* The `^` checks the very first letter, and the `$` checks the very last letter.
* **What it does:** It makes sure the *entire* text is an email. It blocks junk like `"hello a@b.com world"`.

### 2. The Username (`[A-Za-z0-9_]+`)

* Letters, numbers, and underscores (`_`) are fine. The `+` sign means you have to wear *at least one* item.

### 3. The Name Tag (`@{1}`)

*  You must wear exactly one `@` name tag. If you have zero, or two (`@@`), the bouncer laughs and kicks you out.

### 4. The Company Name (`[A-Za-z]*`)

*  **NO NUMBERS ALLOWED.** If your company is "website123", you are rejected. The `*` means it can be any length.

### 5. The Secret Password (`\\.com`)

*  In Regex, a normal dot `.` is a wild card that means "literally anything." We slap it with backslashes `\\` to yell, "No! I just want a normal, boring dot!"
* **What it does:** Forces the email to end with exactly `.com`.
---

### ⏱️ Complexity
**Time Complexity:** *O(N)*  We scan each row in the Users table exactly once. The regex evaluation takes relatively constant time per string based on its length.

**Space Complexity:** *O(1)*  We don't use any extra memory or intermediate data structures, just the output ta


---

## 💻 The Final Code

```sql
/* Write your MySQL query statement below */
SELECT user_id, email
FROM Users
WHERE email REGEXP '^[A-Za-z0-9_]+@{1}[A-Za-z]*\\.com$'
ORDER BY user_id ASC;
```
![UPvote](https://i.imgflip.com/57jfh9.jpg)