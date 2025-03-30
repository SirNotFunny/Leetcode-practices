class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        r = len(digits)-1
        carry = 1
        tmp = 0
        while r >= 0:
            tmp = digits[r] + carry #add carry
            digits[r] = tmp % 10 #insert the initial value of the tmp value
            carry = tmp // 10  #change the carry into the left digit of tmp value
            if not carry:#if there are no carry
                break #end operation
            r-=1 #move to the left digit
        if carry:
            digits.insert(0, carry) #if end the loop and there are still carry, insert the (carry) value to (0) position 
        return digits