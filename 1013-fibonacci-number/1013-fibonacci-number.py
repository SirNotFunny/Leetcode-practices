class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        arr = [0] * (n+1)
        arr[0] = 0
        arr[1] = 1
        for i in range(2, n+1):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n]