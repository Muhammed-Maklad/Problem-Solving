# 3190. Find Minimum Operations to Make All Elements Divisible by Three

**Difficulty:** Easy

[LeetCode Problem](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/)

## Problem

You are given an integer array `nums`. In one operation, you can add or subtract `1` from **any** element of `nums`.

Return the **minimum** number of operations to make all elements of `nums` divisible by `3`.

## Examples

### Example 1

**Input:**

```text
nums = [1, 2, 3, 4]
```

**Output:**

```text
3
```

**Explanation:**

All array elements can be made divisible by `3` using `3` operations:

* Subtract `1` from `1` → `0`
* Add `1` to `2` → `3`
* `3` is already divisible by `3`
* Subtract `1` from `4` → `3`

### Example 2

**Input:**

```text
nums = [3, 6, 9]
```

**Output:**

```text
0
```

**Explanation:**

All elements are already divisible by `3`, so no operations are needed.

## Approach

For each number `x`, we only need to check its remainder when divided by `3`.

* If `x % 3 == 0`, no operation is needed.
* If `x % 3 == 1`, subtracting `1` makes it divisible by `3`.
* If `x % 3 == 2`, adding `1` makes it divisible by `3`.
