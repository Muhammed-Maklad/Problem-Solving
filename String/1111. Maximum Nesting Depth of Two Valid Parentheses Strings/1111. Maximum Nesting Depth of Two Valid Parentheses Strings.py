class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        Parentheses = 0
        res = []

        for x in seq:

            if x == "(":
                res.append(Parentheses % 2)
                Parentheses += 1

            else:
                Parentheses -= 1
                res.append(Parentheses % 2)

        return res