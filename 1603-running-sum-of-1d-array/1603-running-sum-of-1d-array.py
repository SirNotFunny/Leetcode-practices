class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [nums[0]]
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            res.append(nums[i])
        return res
