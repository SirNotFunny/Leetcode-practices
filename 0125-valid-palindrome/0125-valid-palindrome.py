class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newS=""
        for temp in s:
            if temp.isalnum():
                newS+=temp.lower()
        if newS == newS[::-1]: #reverse syntax
            return True
        else:
            return False
