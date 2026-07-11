# 6. Zigzag Conversion

**Problem Link:**  
https://leetcode.com/problems/zigzag-conversion/description/

## Problem Statement

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this:

```text
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line:

```text
PAHNAPLSIIGYIR
```

Write the code that will take a string and make this conversion given a number of rows:

```cpp
string convert(string s, int numRows);
```

---

## Example 1

**Input**

```text
s = "PAYPALISHIRING"
numRows = 3
```

**Output**

```text
PAHNAPLSIIGYIR
```

---

## Example 2

**Input**

```text
s = "PAYPALISHIRING"
numRows = 4
```

**Output**

```text
PINALSIGYAHRPI
```

**Explanation**

```text
P     I    N
A   L S  I G
Y A   H R
P     I
```

---

## Example 3

**Input**

```text
s = "A"
numRows = 1
```

**Output**

```text
A
```

---

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), `','`, and `'.'`
- `1 <= numRows <= 1000`
