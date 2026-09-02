class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        Totoal = sum(x for x in range(1, n+1) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0 )
        return Totoal