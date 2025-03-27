class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = prices[0]
        for sell in prices[1:]: #'1:' is value of sell in the array
            if sell>buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        return profit