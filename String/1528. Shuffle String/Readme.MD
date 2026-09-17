
# 1528. Shuffle String

## Difficulty: Easy

## Description

You are given a string `s` and an integer array `indices` of the **same length**.

The string `s` will be shuffled such that the character at the `ith` position moves to `indices[i]` in the shuffled string.

Return *the shuffled string*.

---

## Examples

### Example 1

**Input:**
```text
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
````

**Output:**

```text
"leetcode"
```

**Explanation:**

Each character in `s` moves to the position specified by `indices[i]`.

```text
Character     Original Index     New Index
-------------------------------------------
    c                0                4
    o                1                5
    d                2                6
    e                3                7
    l                4                0
    e                5                2
    e                6                1
    t                7                3
```

After moving every character to its specified position, the shuffled string becomes:

```text
"leetcode"
```

### Example 2

**Input:**

```text
s = "abc"
indices = [0,1,2]
```

**Output:**

```text
"abc"
```

**Explanation:**

After shuffling, each character remains in its original position.

---

## Constraints

* `s.length == indices.length == n`
* `1 <= n <= 100`
* `s` consists of only lowercase English letters.
* `0 <= indices[i] < n`
* All values of `indices` are **unique**.

```
```
