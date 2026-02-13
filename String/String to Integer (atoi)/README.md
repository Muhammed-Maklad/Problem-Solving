# String to Integer (atoi)
## Difficulty

<span style="color:yellow">**Medium**</span>

## Problem Description

Implement the `atoi` function, which converts a string to an integer. The function discards any leading whitespace characters until the first non-whitespace character is found. Then, it takes an optional initial plus or minus sign followed by numerical digits and interprets them as a numerical value.

### Rules:
1. Discard leading whitespace.
2. Handle optional '+' or '-' sign.
3. Convert numerical digits to an integer.
4. Stop conversion when encountering a non-digit character.
5. Clamp the integer within the range [-2^31, 2^31 - 1].

### Example

#### Example 1:
**Input:**
```
"42"
```
**Output:**
```
42
```

#### Example 2:
**Input:**
```
"   -42"
```
**Output:**
```
-42
```

#### Example 3:
**Input:**
```
"4193 with words"
```
**Output:**
```
4193
```

---

## Constraints

- Input string length: `1 <= s.length <= 200`
- The input string consists of printable ASCII characters.

---

## Notes
This problem is commonly asked in coding interviews and tests your understanding of string parsing and edge case handling.