class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        index_nums = []
        for i in range(0, n):
            index_nums.append(nums[i] +i )

        def check(end):    
            first_index = None
            for i in range(end):      
                if index_nums[i] >=   end:
                    first_index = i
                    return first_index
            return first_index
    
        ans = True

        end = n-1
        while(end != 0 ):
            r = check(end)
            print(r, ans)
            if r == None:
                ans = False
                return ans
            end = r
        
        return ans
            
                