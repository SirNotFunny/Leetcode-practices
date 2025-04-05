class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        n = Counter(ransomNote) # ex: 'aa' = 'a: 2' 
        m = Counter(magazine)
        for char in n:
            if n[char] > m.get(char, 0): #ex: n['a' : 2] > m['a': 3]
                return False
        return True