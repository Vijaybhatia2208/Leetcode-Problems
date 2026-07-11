class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""

        if numRows ==1:
            return s

        rows = 0
        while rows < numRows :
            i = rows
            track =  1
            while i < len(s):
                ans= ans[:len(s)]+ s[i] 
                if rows == 0 or rows == numRows-1:
                    i += (numRows-1) + numRows -1
                else:
                    if track%2==1:
                        track = 0
                        i+= (numRows-rows-1)*2
                    
                    else:
                        track = 1
                        i += rows*2
                
            print(s)
            rows+=1
        
        return ans
    
"PINASGYHPI"
# PAPALISHIRING

"""
PINA
P     I    N
A   L S  I G
Y A   H R
P     I

"""