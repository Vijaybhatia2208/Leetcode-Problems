class Solution:
    def intToRoman(self, num: int) -> str:
        def helper(x, zero):
            # 1
            i = int(x)
            if i == 1 and zero ==0:
                return "I"
            elif i == 1 and zero == 1:
                return "X"
            elif i == 1 and zero == 2:
                return "C"
            elif i == 1 and zero == 3:
                return "M"
            #2
            if i == 2 and zero ==0:
                return "II"
            elif i == 2 and zero == 1:
                return "X"*2
            elif i == 2 and zero == 2:
                return "C"*2
            elif i == 2 and zero == 3:
                return "M"*2
            
            #3
            if i == 3 and zero ==0:
                return "III"
            elif i == 3 and zero == 1:
                return "X"*3
            elif i == 3 and zero == 2:
                return "C"*3
            elif i == 3 and zero == 3:
                return "M"*3
            #4
            if i == 4 and zero ==0:
                return "IV"
            elif i == 4 and zero == 1:
                return "XL"
            elif i == 4 and zero == 2:
                return "CD"
            
            #5
            if i == 5 and zero ==0:
                return "V"
            elif i == 5 and zero == 1:
                return "L"
            elif i == 5 and zero == 2:
                return "D"
            
            #6
            if i == 6 and zero ==0:
                return "VI"
            elif i == 6 and zero == 1:
                return "LX"
            elif i == 6 and zero == 2:
                return "DC"
            
            #7
            if i == 7 and zero ==0:
                return "VII"
            elif i == 7 and zero == 1:
                return "LXX"
            elif i == 7 and zero == 2:
                return "DCC"

            #8
            if i == 8 and zero ==0:
                return "VIII"
            elif i == 8 and zero == 1:
                return "LXXX"
            elif i == 8 and zero == 2:
                return "DCCC"
            
            #9
            if i == 9 and zero ==0:
                return "IX"
            elif i == 9 and zero == 1:
                return "XC"
            elif i == 9 and zero == 2:
                return "CM"

        s = str(num)
        print(s)
        zero = 0
        ans = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] != "0":
                ans = helper(s[i], zero)+ ans
            zero = zero+1
        
        return ans


# 1994
#     3 4 - 4, 0.  - IV
#     2 9 - 9, 1   - IC + IV
#     1 9 - 9,2    -  IM + ICIV
#     0 1 - 1, 3.  -  M + IM+IC+IV
        