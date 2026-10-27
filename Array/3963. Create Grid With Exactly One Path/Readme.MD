# 3963. Create Grid With Exactly One Path

**Difficulty:** Easy
**Constraints:** `1 <= m, n <= 25`

## Problem Description

You are given two integers `m` and `n`, representing the number of rows and columns of a grid.

Construct any `m x n` grid consisting only of the characters `'.'` and `'#'`, where:

- `'.'` represents a free cell.
- `'#'` represents an obstacle cell.

A valid path is a sequence of free cells that:

- Starts at the top-left cell `(0, 0)`.
- Ends at the bottom-right cell `(m - 1, n - 1)`.
- Moves only:
  - **Right:** From `(i, j)` to `(i, j + 1)`.
  - **Down:** From `(i, j)` to `(i + 1, j)`.

Return any grid such that there is **exactly one valid path** from the top-left cell to the bottom-right cell.

## Examples

### Example 1

**Input:**

```text
m = 2, n = 3
```

**Output:**

```text
["..#", "#.."]
```

**Explanation:**

The only valid path is:

```text
(0,0) -> (0,1) -> (1,1) -> (1,2)
```

### Example 2

**Input:**

```text
m = 3, n = 3
```

**Output:**

```text
["..#", "#..", "##."]
```

**Explanation:**

The only valid path is:

```text
(0,0) -> (0,1) -> (1,1) -> (1,2) -> (2,2)
```

### Example 3

**Input:**

```text
m = 1, n = 4
```

**Output:**

```text
["...."]
```

**Explanation:**

The only valid path is:

```text
(0,0) -> (0,1) -> (0,2) -> (0,3)
```

## Constraints

- `1 <= m, n <= 25`

## Notes

- Any grid satisfying the requirements is accepted.
- The grid must contain exactly one valid path from `(0, 0)` to `(m - 1, n - 1)`.
- Movement is restricted to the right and downward directions.
