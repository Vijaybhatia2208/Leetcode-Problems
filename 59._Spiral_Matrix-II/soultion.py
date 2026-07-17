class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = []
        for i in range(0, n):
            helper = []
            for j in range(0, n):
                helper.append(0)
            
            ans.append(helper)
        

        top = 0
        bottom = n-1
        left = 0
        right = n-1
        
        count = 1
        lr = 1
        rl = 0
        tb = 0
        bt = 0

        while count <= n*n:
            if lr ==1:
                i = left
                while i<=right:
                    ans[top][i] = count
                    count+=1
                    i+=1

                top+=1
                lr=0
                tb=1
            
            elif  tb==1:
                i = top
                while i <= bottom:
                    ans[i][right] = count
                    count+=1
                    i+=1
                
                right-=1
                tb=0
                rl=1
            
            elif rl == 1:
                i = right
                while i >= left:
                    ans[bottom][i]= count
                    count+=1
                    i-=1
                
                bottom-=1
                rl=0
                bt=1
            
            elif bt==1:
                i = bottom
                while i>= top:
                    ans[i][left] = count
                    i-=1
                    count+=1

                left+=1
                bt=0
                lr=1
            
        
        return ans 
                



