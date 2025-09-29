class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        index = 0 
        for x in range(len(s)):
            if s[index:]+s[:index] == goal:
                return True
            index += 1
        return False

rTest = Solution()
s ="gcmbf"
goal ="fgcmb"
print(rTest.rotateString(s, goal)) 