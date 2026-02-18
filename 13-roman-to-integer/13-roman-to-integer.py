class Solution:
    def romanToInt(self, s: str) -> int:
        def roman_to_int(val):
            if val == "I":
                return 1
            if val == "V":
                return 5
            if val == "X":
                return 10
            if val == "L":
                return 50
            if val == "C":
                return 100
            if val == "D":
                return 500
            if val == "M":
                return 1000

        def greater(val, val1):
            return roman_to_int(val) < roman_to_int(val1)
        
        ans = 0
        i = 0
        while i < len(s):
            print(i)
            if i < len(s)-1 and greater(s[i],s[i+1]):
                ans = ans + roman_to_int(s[i+1]) - roman_to_int(s[i])
                i = i + 1
            else:
                ans = ans + roman_to_int(s[i])
            i = i +1
        return ans
# MCMXCIV
# last index 6
# i =0  true and 1000 < 100
# false  => 1000
# i=1 true and 1000 > 100
# ans = 1000 + 1000 - 100 -> 1900

# i =3 true 100> 10
# 1990
# i =5
