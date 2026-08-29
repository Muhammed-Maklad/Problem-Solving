class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ""
        for alpha in s :
            if alpha.isalnum() :
                res += alpha.lower()

        return res == res [::-1]