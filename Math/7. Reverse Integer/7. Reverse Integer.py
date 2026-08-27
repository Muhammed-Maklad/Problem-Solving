class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = str(x)[::-1] if x >= 0 else "-" + str(x)[:0:-1]
        num = int(num)

        return num if -2**31 <= num <= 2**31 - 1 else 0