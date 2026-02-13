class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        profit = 0
        for x in range(1, len(prices)):
            if prices[x] < buy :
                buy = prices[x]
            elif prices[x] - buy > profit :
                profit = prices[x] - buy
        return profit 