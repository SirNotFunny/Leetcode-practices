class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 1
        if n==2:
            return 2
        arr = [0] * n
        arr[0] = 1
        arr[1] = 2 #technically fibonacci since the next step will always equal to the sum of ways to get to the 2 lower steps 
        for i in range(2,n):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n-1]