class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) -1
        carry = 0
        res = []
        while i>=0 or j>=0 or carry:
            if i >=0:
                digit1 = int(a[i])
            else:
                digit1 = 0 
            if j>=0:
                digit2 = int(b[j])
            else:
                digit2 = 0
            s =  digit1 + digit2 + carry
            carry = s // 2
            remain = s % 2
            res.append(str(remain))
            i-=1
            j-=1
        return "".join(res[::-1]) #return the "*blank*" then combine all of the reverse res with out it returning as "["0", "0", "1"]" 