class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) #Sum solution ex: sum of ex1 = 4, sum of the range 0-3 is 6 
        for i in range(len(nums)):
            n += (i - nums[i])
        return n
        