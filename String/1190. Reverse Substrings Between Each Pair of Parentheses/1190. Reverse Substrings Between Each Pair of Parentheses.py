class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current = ""

        for x in s:

            if x == "(":
                stack.append(current)
                current = ""

            elif x == ")":
                previous = stack.pop()
                current = current[::-1]
                current = previous + current

            else:
                current += x

        return current
