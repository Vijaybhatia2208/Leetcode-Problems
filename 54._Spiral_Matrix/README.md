# 54. Spiral Matrix

**Problem Link:** https://leetcode.com/problems/spiral-matrix/

**Difficulty:** Medium

## Problem Statement

Given an `m × n` matrix, return all elements of the matrix in **spiral order**.

---

## Example 1

**Input:**

```text
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
```

**Output:**

```text
[1,2,3,6,9,8,7,4,5]
```

---

## Example 2

**Input:**

```text
matrix = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]
```

**Output:**

```text
[1,2,3,4,8,12,11,10,9,5,6,7]
```

---

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`
