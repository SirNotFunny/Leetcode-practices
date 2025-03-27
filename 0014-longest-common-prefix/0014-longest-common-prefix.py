class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_length = float('inf')
        i = 0
        for s in strs:
            if len(s)<min_length: #min len of the smallest word in string array
                min_length = len(s)
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]: #first character of the i-th word
                    return s[:i] # ":i" is "up until i"
            i+=1
        return s[:i]