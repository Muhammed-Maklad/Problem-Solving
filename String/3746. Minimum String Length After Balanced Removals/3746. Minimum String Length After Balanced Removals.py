class Solution(object):
    def minLengthAfterRemovals(self, s):
        """
        :type s: str
        :rtype: int
        """
        CountA = s.count("a")
        return abs(2*CountA - len(s))