class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        start = 1
        num1 = 0
        num2 = 0
        for x in range(start, n+1):
            if x % m == 0 :
                num2 += x
            else:
                num1 += x

        return(num1-num2)