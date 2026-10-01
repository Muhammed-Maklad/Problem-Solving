class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for chr in s :
            if chr in "([{":
                stack.append(chr)

            else:
                if not stack:
                    return False

                top = stack.pop()
                if chr == ')' and top != '(':
                    return False
                if chr == ']' and top != '[':
                    return False
                if chr == '}' and top != '{':
                    return False
        return not stack