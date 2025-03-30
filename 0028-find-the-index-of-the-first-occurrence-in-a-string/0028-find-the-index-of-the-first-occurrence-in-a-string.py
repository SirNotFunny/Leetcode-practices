class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        x = len(haystack)
        y = len(needle)
        for i in range(x-y+1):
            if haystack[i:i+y] == needle:
                return i
        return -1