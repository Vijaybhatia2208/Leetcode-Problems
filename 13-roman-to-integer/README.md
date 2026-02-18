# Roman to Integer

Roman numerals are represented by seven symbols:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are usually written from largest to smallest from left to right.  
However, some numbers use subtraction:

- I before V or X → 4, 9
- X before L or C → 40, 90
- C before D or M → 400, 900

## Problem

Given a Roman numeral string `s`, convert it to an integer.

---

## Examples

### Example 1

**Input:**  
`s = "III"`  
**Output:**  
`3`

### Example 2

**Input:**  
`s = "LVIII"`  
**Output:**  
`58`  
**Explanation:** L = 50, V = 5, III = 3

### Example 3

**Input:**  
`s = "MCMXCIV"`  
**Output:**  
`1994`  
**Explanation:** M = 1000, CM = 900, XC = 90, IV = 4

---

## Constraints

- `1 <= s.length <= 15`
- `s` contains only: `I, V, X, L, C, D, M`
- `s` is guaranteed to be a valid Roman numeral in range `[1, 3999]`

**Link :** https://leetcode.com/problems/roman-to-integer/description/
