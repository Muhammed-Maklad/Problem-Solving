# Letter Combinations of a Phone Number

## Difficulty: Medium

## Problem Description

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

```
2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuv
9 -> wxyz
```

## Examples

### Example 1:
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

### Example 2:
```
Input: digits = ""
Output: []
```

### Example 3:
```
Input: digits = "2"
Output: ["a","b","c"]
```

## Constraints
- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`

## Solution Approach
The solution uses an iterative approach to build letter combinations:
1. Create a mapping of digits to their corresponding letters
2. For each digit in the input string:
   - If result list is empty, add all letters of current digit
   - Otherwise, combine each previous result with each letter of current digit
3. Return the final list of combinations