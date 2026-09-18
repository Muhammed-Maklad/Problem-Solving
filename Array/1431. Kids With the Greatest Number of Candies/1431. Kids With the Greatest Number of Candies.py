class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        MaxCh= max(candies)
        res = [True if x + extraCandies >= MaxCh else False for x in candies]

        return res