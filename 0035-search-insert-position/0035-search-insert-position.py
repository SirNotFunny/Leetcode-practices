class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)
        while l<r:
            tmp = (l+r) // 2 #middle num
            if nums[tmp] == target:
                return tmp #return tmp if tmp = target
            if nums[tmp] < target:
                l = tmp + 1 #target larger => discard the left half
            else:
                r = tmp #target smaller => discard the right half
        return l #when loop exit, the only value left that is correct and goin from l to r is value: l