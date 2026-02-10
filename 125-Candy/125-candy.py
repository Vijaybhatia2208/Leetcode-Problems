class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l_r = [1]*n
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1] :
                l_r[i] = l_r[i-1] + 1
        

        for i in range(n-2, -1,-1):
            if ratings[i] > ratings[i+1] :
                if l_r[i+1] >= l_r[i] :
                    l_r[i] = l_r[i+1] + 1
        

        return sum(l_r)

        


	   