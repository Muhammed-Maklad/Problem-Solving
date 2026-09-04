# 2553. Separate the Digits in an Array

**Difficulty:** Easy

**Topics:** Array, Math

🔗 [LeetCode Problem](https://leetcode.com/problems/separate-the-digits-in-an-array/)

## Problem

Given an array of positive integers `nums`, return an array `answer` that consists of the digits of each integer in `nums` after separating them in the **same order** they appear in `nums`.

To separate the digits of an integer is to get all the digits it has in the same order.

For example, the separation of `10921` is:

```text
[1, 0, 9, 2, 1]
```

## Examples

### Example 1

**Input:**

```text
nums = [13,25,83,77]
```

**Output:**

```text
[1,3,2,5,8,3,7,7]
```

**Explanation:**

* The separation of `13` is `[1,3]`.
* The separation of `25` is `[2,5]`.
* The separation of `83` is `[8,3]`.
* The separation of `77` is `[7,7]`.

Therefore:

```text
answer = [1,3,2,5,8,3,7,7]
```

The digits appear in the same order as the original numbers.

### Example 2

**Input:**

```text
nums = [7,1,3,9]
```

**Output:**

```text
[7,1,3,9]
```

**Explanation:**

Each integer contains only one digit, so the separation of each integer is itself.

## Constraints

* `1 <= nums.length <= 1000`
* `1 <= nums[i] <= 10^5`


```
