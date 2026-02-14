solution = 1
n = 2

def cal (n):
    if n == 0 or n == 1:
        return 1
    else:
        return cal(n - 1) +  cal(n - 2)
    

print(cal(2))
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def cal (n):
            if n == 0 or n == 1:
                return 1
            else:
                return cal(n - 1) +  cal(n - 2)
        cal(n)
    