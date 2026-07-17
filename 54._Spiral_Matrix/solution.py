class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix) 
        m = len(matrix[0])
        top = 0
        bottom = n-1
        left = 0
        right = m -1

        lr = 1
        tb = 0
        rl = 0
        bt = 0
        count = 0
        ans = []
        while count < (m*n):
            if lr == 1:
                i =  left
                while i<=right:
                    ans.append(matrix[top][i])
                    count+=1
                    i+=1

                top+=1
                lr=0
                tb=1

            elif tb==1:
                i = top
                while i<=bottom:
                    ans.append(matrix[i][right]) 
                    count+=1
                    i+=1 
                
                right-=1
                tb=0
                rl=1
            
            elif rl==1:
                i = right
                while i >= left:
                    ans.append(matrix[bottom][i])
                    count+=1
                    i-=1
                
                bottom-=1
                rl=0
                bt=1
            
            elif bt ==1:
                i= bottom
                while i>=top:
                    ans.append(matrix[i][left])
                    count+=1
                    i-=1
                
                left+=1
                bt=0
                lr=1
            
        

        return ans
