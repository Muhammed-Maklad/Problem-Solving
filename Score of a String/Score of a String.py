class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0

        for x in range(1, len(s)):
            res += abs(ord(s[x-1])- ord(s[x]))

        return res