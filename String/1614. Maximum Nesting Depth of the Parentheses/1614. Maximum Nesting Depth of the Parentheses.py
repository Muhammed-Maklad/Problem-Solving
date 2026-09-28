class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        level , maxLevel = 0 , 0

        for x in s:
            level += (x == "(") - (x == ")")
            maxLevel = max(maxLevel, level)

        return maxLevel