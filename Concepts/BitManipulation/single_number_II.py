"""

Contribution technique
Given an array every element repeat 3 time and this element repeat once

A: [5,7,5,4,7,11,11,9,11,7,5,4,4]

We can do this using
BF      => TC: O(N^2) , SC: O(1)
Hasmap  => TC: O(N) , SC: O(n)
Sort    => TC: O(NLogN), SC: O(1)
Bitwise => TC: o(N), SC: O(1)

5   =>  0101
7   =>  0111
5   =>  0101
4   =>  0100
7   =>  0111
11  =>  1011
11  =>  1011
9   =>  1001
11  =>  1011
7   =>  0111
5   =>  0101
4   =>  0100
4   =>  0100
position 3210 
0th position=>    11    (no. of set bits)    11%3 => 1    
1th position=>    6    (no. of set bits)     6%3. => 0
2th position=>    9    (no. of set bits)     9%3  => 0
3th position=>    4    (no. of set bits)     4%3. => 1
ANS = 1001 > 9


[-2,-2,1,1,4,1,4,4,-4,-2]

[43,16,45,89,45,-2147483648,45,2147483646,-2147483647,
-2147483648,43,2147483647,-2147483646,-2147483648,89,-2147483646,89,
-2147483646,-2147483647,2147483646,-2147483647,16,16,2147483646,43]
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        max_el = 32
        # we have to take 32 bit because -ve is there
        ans = 0
        index = 0
        while max_el > 0:
            count = 0
            for _, value in enumerate(nums):
                if value & 1<<index > 0:
                    count+=1
            
            if count %3 >0 :
                ans = ans + (1<<index)
            
            # print(index,count, ans)
            max_el-=1
            index+=1
        
        if ans & 1<<31 > 0 :
            return ans -(1<<32)
        return ans

