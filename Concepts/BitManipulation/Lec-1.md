2^0+ 2^1 + 2^2 + 2^3+ ....... +2^k = 2^k+1 -1

- Sum of GP = a(r^t -1) / (r-1)

a = 1,
r = 2
t = k+1 (number of terms)

sum = 1(2^k+1 -1) / (2-1) = (2^k+1) -1

## Number System

1. Decimal number system

symbols = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
base = 10

3462 = 3* 1000 + 4 * 100 + 6*10 + 2 *1

2. Binary number system

symbols = 0, 1
Base = 2

12101 => Non binary number
10101 => 1* 2^4+ 0* 2^3 + 1* 2^2 + 0* 2^1 + 1\*2^0 = 21

## Bitwise Operations

- AND
- OR
- XOR
- NOT
- Shift

& , ~, | we all understand

,>>, << is uterarchy operator

a = 29 -> 11101
b = 18 -> 10010

a|b. -> 11111
a&b. -> 10000
a^b. -> 01111

left shift:
a: 5 , 00000101 -> 2^2+ 2^0

a<<1 -> 2(2^2+ 2^0) = 2^3 + 2^1 =10

int -> 4 byte -> 32 bits
long -> 8 byte -> 64 bits

**_ Every time we left shit it value 2 number _**

n<<k => n\2^k

Right shift:
a = 5
101
a>>1 -> 5/ 2^1 = 2
a>>2 -> 5/ 2^2 = 1
a>>3 -> 5/ 2^3 = 0

**_ Every time we right shit it value 2 number _**

n>>k => n/2^k

Avg(a,b) = a+b/2 = (a+b)>>1

## Question 1

**_ Given an integer N, check if ith bit is set or not _**

N=25 -> 11001

n & (1<<pos)

if n & (1<<pos) > 0 then ith bit is set
else ith bit is not set

## Question 2

**_ Given an integer N, flip the ith bit _**

N = 25 -> 11001

n ^ (1<<pos)

if n & (1<<pos) > 0 then ith bit is set

## Question 3

**_ Given an integer N, return the number of set bits _**

N =64. ->1000000
N= 31 -> 0011111

## Given N. check if it is power of 2

N= 32
Pow(2) = 1set bit
if n& n-1 == 0 :
print("Power of 2")

## Given N Number, Every Element Repeats except 1 element , find that

A: [3,2,3,4,6,4,2]
XOR of all number is answer

## 137. Single Number II

- Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
  https://leetcode.com/problems/single-number-ii/description/
