num = 2
sum = 3


class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        res = ""
        if sum > 9 or sum < 0 :
            return ""

        for x in range(num):
            digit = min(9,sum)
            sum -= digit
            res += digit
        return res