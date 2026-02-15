class Solution:
    def reverseWords(self, s: str) -> str:
        space = [-1]

        for i in range(0, len(s)):
            if s[i] == " ":
                space.append(i)
        
        if len(space) == 1:
            return s

        ans = []
        for i in range(0, len(space)):
            curr= space[i]
            if i == len(space)-1 and i < len(s)-1:
                if s[curr+1:len(s)] == "" or s[curr+1:len(s)] == " ":
                    continue
                else:
                    ans.append(s[curr+1:len(s)])   
            elif i== len(s) -1:
                continue
            else:
                if s[curr+1:space[i+1]] == "" or s[curr+1:space[i+1]] == " ":
                    continue
                else:
                    ans.append(s[curr+1:space[i+1]])
                    if space[i+1] == len(s)-1:
                        continue
                    else:
                        ans.append(" ")

        ans_str = ""


        for i in range(len(ans)-1, -1, -1):
            if i == len(ans)-1 and ans[i] == " ":
                continue
            else:
                ans_str = ans_str + ans[i]
            print(ans[i])
            
        return ans_str