class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        tmp = triangle[-1]
        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                tmp[col] = min(tmp[col], tmp[col + 1]) + triangle[row][col]
        return tmp[0]