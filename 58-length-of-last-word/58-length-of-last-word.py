class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = []
        i = 0
        j = 0
        while j < len(s):
            if s[j] == " ":
                print(i, j)
                print(s[i:j])
                index.append(s[i:j])
                i=j+1
            j=j+1
        
        print(j)
    
        if i < len(s):
            index.append(s[i:len(s)])

        print(index)
        if len(index) == 0:
            return s
        else :
            for i in range(len(index)-1, -1,-1):
                if index[i] != "" and index[i]!=" ":
                    return len(index[i])

        
# " fly me to "
# i =0, j=0 j++
# i =0, j=1 

