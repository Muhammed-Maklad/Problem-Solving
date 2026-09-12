# 3895. Count Digit Appearances

<a href="https://leetcode.com/problems/count-digit-appearances/">
  <img src="https://img.shields.io/badge/LeetCode-3895-orange?style=for-the-badge&logo=leetcode" alt="LeetCode 3895">
</a>

<img src="https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge" alt="Medium">

---

## Problem

You are given an integer array `nums` and an integer `digit`.

Return the total number of times `digit` appears in the decimal representation of all elements in `nums`.

---

## Example 1

**Input:**

```text
nums = [12,54,32,22], digit = 2
```

**Output:**

```text
4
```

**Explanation:**

The digit 2 appears once in 12 and 32, and twice in 22. Thus, the total number of times digit 2 appears is 4.

---

## Example 2

**Input:**

```text
nums = [1,34,7], digit = 9
```

**Output:**

```text
0
```

**Explanation:**

The digit 9 does not appear in the decimal representation of any element in `nums`, so the total number of times digit 9 appears is 0.

---

## Constraints

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 106`
* `0 <= digit <= 9`
