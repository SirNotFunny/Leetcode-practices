class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxWealth = 0
        for i in range(len(accounts)):
            count = 0
            for j in range(len(accounts[0])):
                count += accounts[i][j]
                if count > maxWealth:
                    maxWealth=count
        return maxWealth