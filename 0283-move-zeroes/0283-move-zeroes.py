class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        tmp = 0
        for i in range(len(nums)):
            if nums[i] != 0: #if the value is not 0
                nums[tmp], nums[i] = nums[i], nums[tmp] #swap
                tmp+=1
        return nums