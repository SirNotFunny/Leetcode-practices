class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = 0
        n=len(nums)
        for i in range(n-1):
            if nums[i] != 0 and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        for i in range(n):
            if nums[i] != 0:
                nums[tmp], nums[i] = nums[i], nums[tmp]
                tmp+=1
        return nums