# 20. Valid Parentheses

**Difficulty:** Easy

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

A string is considered **valid** if:

1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every closing bracket has a corresponding opening bracket of the same type.

---

## Examples

### Example 1

**Input:**

```text
s = "()"
```

**Output:**

```text
true
```

---

### Example 2

**Input:**

```text
s = "()[]{}"
```

**Output:**

```text
true
```

---

### Example 3

**Input:**

```text
s = "(]"
```

**Output:**

```text
false
```

---

### Example 4

**Input:**

```text
s = "([])"
```

**Output:**

```text
true
```

---

### Example 5

**Input:**

```text
s = "([)]"
```

**Output:**

```text
false
```

---

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists only of the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`.
