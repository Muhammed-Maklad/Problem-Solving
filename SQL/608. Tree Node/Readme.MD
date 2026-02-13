
# Tree Node
## Difficulty

![Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem Description

You are provided with a database table named `Tree` that represents a hierarchical tree structure. Each row contains an `id` (the node's identifier) and a `p_id` (the parent node's identifier).

Your task is to determine the "type" of every node in the tree based on its relationship with other nodes. The result must list each node's `id` and its corresponding `type`.

## Rules

Each node can be classified into one of the following three types:

1. **Root**: The node has no parent (its `p_id` is `null`).
2. **Inner**: The node has a parent and serves as a parent to at least one other node.
3. **Leaf**: The node has a parent but does not serve as a parent to any other node.

## Examples

### **Example 1**

Input:


Tree table:

| id | p_id |
----|------
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |



Output:


| id | type  |
----|-------
| 1  | Root  |
| 2  | Inner |
| 3  | Leaf  |
| 4  | Leaf  |
| 5  | Leaf  |



### Example 2

Input:

Tree `table`:

| id | p_id |
----|------
| 1  | null |




**Output:**


| id | type  |
----|-------
| 1  | Root  |


## Constraints

* `id` is the column with unique values.
* The `p_id` column may contain `null` values.
* The given data structure is guaranteed to be a valid tree.

## Notes

This problem tests your ability to handle hierarchical data in SQL. It specifically focuses on:

* Using conditional logic (`CASE WHEN`) to categorize data.
* Handling `NULL` values correctly (specifically for the Root node).
* Using subqueries or `IN` / `NOT IN` clauses to determine parent-child relationships.

