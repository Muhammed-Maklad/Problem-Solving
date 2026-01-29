# 228. Summary Ranges
**Difficulty:** Easy

---

## Problem Statement

You are given a sorted array of unique integers nums. Return the smallest sorted list of ranges that cover all the numbers in the array. Each range [a, b] should be output as:
- "a->b" if a != b
- "a" if a == b

## Examples
- Input: nums = [0,1,2,4,5,7]
  - Output: ["0->2","4->5","7"]
- Input: nums = [0,2,3,4,6,8,9]
  - Output: ["0","2->4","6","8->9"]
- Input: nums = []
  - Output: []
- Input: nums = [-1]
  - Output: ["-1"]

## Constraints
- 0 <= nums.length <= 20
- -2^31 <= nums[i] <= 2^31 - 1
- nums is sorted in ascending order
- nums contains no duplicates

