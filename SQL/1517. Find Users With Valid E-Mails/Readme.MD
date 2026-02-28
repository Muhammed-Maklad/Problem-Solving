
## 🧠 Intuition

When building a robust backend system, validating user inputs like email addresses is a classic task. Standard SQL `LIKE` operators just aren't powerful enough to enforce complex string rules. This is exactly where **Regular Expressions (REGEXP)** shine!

The problem gives us very specific rules for what makes an email valid:

1. The prefix must **start with a letter**.
2. The prefix can only contain letters, numbers, underscores `_`, periods `.`, and dashes `-`.
3. The domain must be exactly `@leetcode.com`.

---

## 🚀 Approach: Step-by-Step Regex Breakdown

### Step 1: Nailing the Prefix Start

The rule says the email *must* start with a letter. In regex, we write this as:

* `^` means "start of the string".
* `[A-Za-z]` means "any single uppercase or lowercase letter".

Putting it together, `^[A-Za-z]` ensures the very first character is strictly a letter.

### Step 2: Allowing the Right Characters

After the first letter, the prefix can have a mix of specific characters.

* `[A-Za-z0-9._-]` defines our allowed list (letters, digits, dot, underscore, dash).
* `*` means "zero or more of the preceding characters".

So, `[A-Za-z0-9._-]*` handles the rest of the user's name right up until the `@` symbol.

### Step 3: Locking in the Domain

The email must end perfectly with `@leetcode.com`.

* `@leetcode` is just plain text.
* `\\.` is used because a single dot `.` is a special character in regex that means "any character". We use the backslashes to "escape" it, telling SQL we want a literal dot.
* `com$` uses the `$` symbol, which means "end of the string".

Combined Regex: `'^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$'`

### Step 4: The `LIKE BINARY` Trap (Crucial Detail!)

You might wonder why we need the second part of the `WHERE` clause. In MySQL, the `REGEXP` operator is **case-insensitive** by default. This means it would happily accept `@LeetCode.com` or `@LEETCODE.COM`—which LeetCode considers invalid!

To force the database to check the exact, lowercase spelling of the domain, we use a clever trick:
`AND mail LIKE BINARY '%@leetcode.com'`

---

## 🧾 Code

```sql
/* Write your MySQL query statement below */
SELECT *
FROM Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$'
    AND mail LIKE BINARY '%@leetcode.com';

```

