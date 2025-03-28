class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]: #range from 1 so we have to check for position #0
                nums[j] = nums[i] #sorted array => check the forward num with the prev num 
                j+=1
        return j
