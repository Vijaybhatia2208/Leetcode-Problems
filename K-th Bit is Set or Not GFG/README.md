#  K-th Bit is Set or No

## Easy
Given a number n and a bit number k, check if the kth index bit of n is set or not. A bit is called set if it is 1. The position of set bit '1' should be indexed starting with 0 from the LSB side in the binary representation of the number.
Note: Index is starting from 0. You just need to return true or false.

### Example 1:
```markdown
Input:
n = 4, k = 0

Output:
false

Explanation: Binary representation of 4 is 100, in which 0th index bit from LSB is not set. So, return false.
```

### Example 2:
```markdown
Input:
n = 4, k = 2

Output:
true

Explanation: Binary representation of 4 is 100, in which 2nd index bit from LSB is set. So, return true.
```

## Constraints:
- `1 ≤ n ≤ 10^9`
- `0 ≤ k ≤ 31`


## Related Topics
- Bitwise

## Links
- [GFG Problem](https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1)

