# 125. Valid Palindrome

**Difficulty:** Easy


## Problem

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.

## Examples

### Example 1

```text
Input:  s = "A man, a plan, a canal: Panama"
Output: true

Explanation:
"amanaplanacanalpanama" is a palindrome.
```

### Example 2

```text
Input:  s = "race a car"
Output: false

Explanation:
"raceacar" is not a palindrome.
```

### Example 3

```text
Input:  s = " "
Output: true

Explanation:
s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

## Constraints

* `1 <= s.length <= 2 * 10^5`
* `s` consists only of printable ASCII characters.

## Approach

Use the **two-pointer** technique:

1. Start one pointer at the beginning of the string and another at the end.
2. Skip any non-alphanumeric characters.
3. Compare the characters after converting them to lowercase.
4. If they are different, return `false`.
5. Move both pointers toward the center.
6. If the pointers meet without finding a mismatch, return `true`.

### Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`
