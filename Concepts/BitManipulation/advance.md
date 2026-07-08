## Given N elements every elements repeats twice except for 2 elements which occur exactly one

https://leetcode.com/problems/single-number-ii/
A: [3,6,4,4,3,8]
Contibution technique

5 => 0101
7 => 0111
4 => 0100
7 => 0111
11 => 1011
11 => 1011
9 => 1001
13 => 1101
5 => 0101
4 => 0100

based on bit we will classify it in Box 1 Box 2
Xor of all array unique item xor 9^13

9 - 1001
13- 1101
xor 0100

we know that this bit is different so we can classify based on this bit for two numbers:
assume i thh bit
let's start with ith bit (if we don;t find diff move to next div)
Box 1: 5, 7,4,7,5,4, 13
Box 2: 11,11,9

if you see both number are seperate with pairs
Xor of Box 1 give you number 1
Xor of Box 2 give you number 2

```

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for _, value in enumerate(nums):

            xor = xor ^ value

        # first index where bit is 1
        print(xor)
        index = 0
        i = 0
        x=32
        while x>0:
            if xor & 1 > 0:
                index=i
                break
            xor = xor>>1
            i+=1
            x-=1

        box1 = 0
        box2 = 0
        print(index)
        for _, value in enumerate(nums):
            if value & (1<<index) > 0:
                box1 = box1 ^ value
            else :
                print(value)
                # print("box2 ", value)
                box2 = box2 ^ value

        return [box1, box2]
```

## Given an array of size N, Array contains all elements in [1, N+2], except 2 elements , Find the missing 2 elements

N=4
[3,6,1,4]

3 011
6 110
1 001
4 100

XOR of [1,2,3,4,5,6] , [3,6,1,4]
xor 2^5

Simple
xor
for i in range(0, n+2):
xor = xor^i

for \_, val enumerate(arr):
xor = xor ^ val

xor left will be 2^5

## XOR sum Given an array of N element calculate the xor sum of all pairs

[3, 5,6,8,2]

3^3 3^5 3^6 3^8 3^2
5^3 5^5 5^6 5^8 5^2
6^3 6^5 6^6 6^8 6^2
8^3 8^5 8^6 8^8 8^2
2^3 2^5 2^6 2^8 2^2

3^3 + 5^5 + 6^6 +8^8 + 2^2 = 0

ans = 2(
3^5 + 11 ^ 101 -> 110 - 6
3^6 + 011 ^ 110 -> 101 - 5
3^8 + 11^ 1000 -> 1011 - 11
3^2 +. - 1
5^6 +. 11 - 3
5^8 +. 1101 -13
5^2 +. 111 - 7
6^8 +. 1110 - 14
6^2 +. 100 - 4
8^2. 1010 - 10
)
=2(74) = 148

TC = O(n^2)
SC = O(1)

observation soln

3 0011
5 0101
6 0110
8 1000
2 0010 4666. combination of set bits for each pair(no. of set bit \* no of non set bit)

ans = 2*(pow(2,3)* 4 +pow(2,2)_ 6 +pow(2,1)_ 6 +pow(2,0)\_6)
= 2* (32+24+12+6)
= 2*74 = 128

## Given an array find the max value of A[i]&A[j] for all (i,j) & i !=j

[27, 18, 20]

27 - 11011
18 - 10010
20 0 10100

27 & 18 - 10010 - 18
27 & 20 - 10000 - 16
18 & 20 - 10000 - 16

18 ans
4 0100
8 1100
3 0011
5 0001

eliminate number from right side if set_bite > 1 eliminate all non-setbit
26 11010
13 01010 elminate
23 10111
28 11100
27 11011
7 00111 elimiate
25 11001

26 11010
23 10111 - eleminat
28 11100
27 11011
25 11001

26 11010
28 11100
27 11011
25 11001

nothing eleminated next bit

26 11010
28 11100 - eliminate
27 11011
25 11001 - eliminate

26&27 -11010-> 26
