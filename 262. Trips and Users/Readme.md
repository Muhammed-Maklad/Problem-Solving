# 262. Trips and Users  
## **Difficulty:** Hard



## Problem Statement

You are given two tables: **Trips** and **Users**.

### Table: Trips

| Column Name | Type    |
|------------|---------|
| id         | int     |
| client_id  | int     |
| driver_id  | int     |
| city_id    | int     |
| status     | enum    |
| request_at | varchar |

- `id` is the primary key.
- The table holds all taxi trips.
- Each trip has a unique `id`.
- `client_id` and `driver_id` are foreign keys to `users_id` in the **Users** table.
- `status` is an ENUM of: `'completed'`, `'cancelled_by_driver'`, `'cancelled_by_client'`.

### Table: Users

| Column Name | Type |
|------------|------|
| users_id   | int  |
| banned     | enum |
| role       | enum |

- `users_id` is the primary key.
- The table holds all users.
- `role` is an ENUM of: `'client'`, `'driver'`, `'partner'`.
- `banned` is an ENUM of: `'Yes'`, `'No'`.

---

The **cancellation rate** is computed as:

> (Number of canceled requests by unbanned users) / (Total number of requests by unbanned users) on that day

A request is considered **valid** only if **both the client and the driver are not banned**.

---

## Task

Write a solution to find the **cancellation rate** of requests with unbanned users for each day between:

- `"2013-10-01"` and `"2013-10-03"`

Only include days that have **at least one trip**.  
Round the **Cancellation Rate** to **two decimal places**.

Return the result table in **any order**.

---

## Example

### Input

**Trips** table:

| id | client_id | driver_id | city_id | status              | request_at |
|----|-----------|-----------|---------|---------------------|------------|
| 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
| 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
| 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
| 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
| 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
| 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
| 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
| 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
| 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
| 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |

**Users** table:

| users_id | banned | role   |
|----------|--------|--------|
| 1        | No     | client |
| 2        | Yes    | client |
| 3        | No     | client |
| 4        | No     | client |
| 10       | No     | driver |
| 11       | No     | driver |
| 12       | No     | driver |
| 13       | No     | driver |

---

### Output

| Day        | Cancellation Rate |
|------------|-------------------|
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |

---

### Explanation

**On 2013-10-01:**
- There were 4 requests in total, 2 were canceled.
- The request with `Id = 2` was made by a banned client, so it is ignored.
- That leaves 3 valid requests, 1 of which was canceled.
- Cancellation Rate = 1 / 3 = **0.33**

**On 2013-10-02:**
- There were 3 requests in total, 0 were canceled.
- The request with `Id = 6` was made by a banned client, so it is ignored.
- That leaves 2 valid requests, 0 canceled.
- Cancellation Rate = 0 / 2 = **0.00**

**On 2013-10-03:**
- There were 3 requests in total, 1 was canceled.
- The request with `Id = 8` was made by a banned client, so it is ignored.
- That leaves 2 valid requests, 1 canceled.
- Cancellation Rate = 1 / 2 = **0.50**
