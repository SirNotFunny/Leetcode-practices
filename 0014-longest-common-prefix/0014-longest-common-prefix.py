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
        while i < min_length: #i mean.. if there is a word with 3 letters in an array with 3+ word, the maximum amount of identical prefix is also 3...
            for s in strs:
                if s[i] != strs[0][i]: #first character of the i-th word
                    return s[:i] # ":i" is "up until i"
            i+=1 #move to next word
        return s[:i]