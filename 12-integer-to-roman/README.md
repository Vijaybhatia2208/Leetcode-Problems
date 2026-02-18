# Integer to Roman

Roman numerals use the following symbols:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are formed by converting decimal place values from highest to lowest using these rules:

- If the value does not start with **4 or 9**, select the largest symbol that can be subtracted and append it to the result.
- If the value starts with **4 or 9**, use the subtractive form:
  - 4 → IV
  - 9 → IX
  - 40 → XL
  - 90 → XC
  - 400 → CD
  - 900 → CM
- Symbols representing powers of 10 (`I`, `X`, `C`, `M`) can be repeated at most **3 times**.
- Symbols `V`, `L`, and `D` cannot be repeated.
- If a symbol would be repeated 4 times, use the subtractive form instead.

## Problem

Given an integer `num`, convert it to a Roman numeral.

---

## Examples

### Example 1

**Input:**  
`num = 3749`  
**Output:**  
`"MMMDCCXLIX"`

**Explanation:**

- 3000 = MMM
- 700 = DCC
- 40 = XL
- 9 = IX

---

### Example 2

**Input:**  
`num = 58`  
**Output:**  
`"LVIII"`

**Explanation:**

- 50 = L
- 8 = VIII

---

### Example 3

**Input:**  
`num = 1994`  
**Output:**  
`"MCMXCIV"`

**Explanation:**

- 1000 = M
- 900 = CM
- 90 = XC
- 4 = IV

---

## Constraints

- `1 <= num <= 3999`

**Link:** https://leetcode.com/problems/integer-to-roman/
