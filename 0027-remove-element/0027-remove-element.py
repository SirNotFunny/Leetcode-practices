class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        j = 0
        for i in range(0, n):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1
        return j