# 🧬 SQL DNA Detective: Cracking the Genetic Code Step-by-Step 🔍

## [UPvote ME](https://leetcode.com/problems/dna-pattern-recognition/solutions/7620933/stop-overcomplicating-string-matching-th-z2u2)

---

### 📋 Step 1: Grab the Basics

First, we just need to select the standard columns the problem asks us to return: the ID, the DNA string itself, and the species.

```sql
SELECT *
```

### 🚪 Step 2: The "Front Door" Scanner (Starts with ATG)

**The Logic:** We need to know if the sequence starts with `ATG`. The `%` is a wild card that means "literally anything can come after." So, `ATG%` translates to "Starts with ATG, and I don't care what the rest of it is."

```sql
       dna_sequence LIKE 'ATG%' AS has_start,

```

### 🏁 Step 3: The "Back Door" Check (Ends with TAA, TAG, TGA)

**The Logic:** Instead of scanning the whole string, we use `RIGHT(dna_sequence, 3)` to cleanly slice off just the last 3 letters. Then, we use `IN (...)` to ask: "Are those 3 sliced letters either TAA, TAG, or TGA?"

```sql
       RIGHT(dna_sequence, 3) IN ('TAA', 'TAG', 'TGA') AS has_stop,

```

### 🫣 Step 4: The "Hide & Seek" Radar (Contains ATAT)

**The Logic:** The pattern `ATAT` could be anywhere—at the front, the back, or right in the middle. By putting the `%` wildcard on *both* sides (`%ATAT%`), we tell SQL: "I don't care what comes before or after, just trigger a `1` if you see `ATAT` hiding anywhere inside!"

```sql
       dna_sequence LIKE '%ATAT%' AS has_atat,

```

### 🚨 Step 5: The "Triple G" Alarm (Contains GGG)

**The Logic:** Just like the step above, we put `%` on both sides to search the entire string. If the database spots at least three `G`s right next to each other (even if it's `GGGG`), it returns a `1`.

```sql
       dna_sequence LIKE '%GGG%' AS has_ggg

```

## 💻 The Final Assembled Code

When you glue all those perfectly logical steps together, you get this beautiful, optimized query:

```sql
/* Write your MySQL query statement below */
SELECT *,
       dna_sequence LIKE 'ATG%' AS has_start,
       RIGHT(dna_sequence, 3) IN ('TAA', 'TAG', 'TGA') AS has_stop,
       dna_sequence LIKE '%ATAT%' AS has_atat,
       dna_sequence LIKE '%GGG%' AS has_ggg
FROM Samples
ORDER BY sample_id ASC;
```

![UPvote](https://i.imgflip.com/57jfh9.jpg)


