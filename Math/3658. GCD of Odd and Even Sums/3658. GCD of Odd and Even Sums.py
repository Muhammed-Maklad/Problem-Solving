class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        # SumOdd = sum(range(1, 2*n, 2))
        # SumEven = sum(range(2, 2*n , 2))
        # return  SumOdd -SumEven 
        return n