class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0 #maximum length
        tmp = {} #index of item
        j= -1 #temporary value
        for i, c in enumerate(s): #current index and current char
            j = max(j, tmp.get(c,-1)) #to check if we have seen that index before, if it we have: j = j, if we havent as in if c hasn't been seen yet, return -1 => j = -1 => the answer get plus 1
            ans = max(ans, i-j) #if the last answer is larger, ans doesnt change, if i-j (which is current index answer + 1) IS larger than previous ans, take it instead. ie: previous ans is 3, the next substring got 4 => take the sub string value
            tmp[c] = i #update the last seen index
        return ans
