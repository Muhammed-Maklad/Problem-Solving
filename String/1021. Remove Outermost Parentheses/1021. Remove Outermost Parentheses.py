class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        depth = 0

        for x in s:
            if x == "(":
                if depth > 0:
                    res += x
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res += x
                    
        return res