class Solution(object):
    @staticmethod
    def maximumDifference( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 0
        sum = 0
        for index in range(1, len(nums)):
            sum = sum + nums[index] - nums[index-1]
            maximum = max(sum, maximum)
            if sum < 0: 
                sum = 0

        return maximum if maximum > 0 else -1

print(Solution.maximumDifference([2, 3, 10, 6, 4, 8, 1]))