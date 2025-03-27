class Solution(object):
    def singleNumber(self, nums):
        count = Counter(nums) #also in hashset but for counting
        for num in count:
            if count[num] == 1:
                return num
        