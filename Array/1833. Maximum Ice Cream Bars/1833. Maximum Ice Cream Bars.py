class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        num = 0
        costs.sort()
        for cost in costs:
            if cost > coins:
                break
            num += 1
            coins -= cost
        return num