class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        index , res = 1 , 0
        for char in s:
            Assci = 26 - (ord(char) % 97) 
            res += Assci*index
            index+=1
        return res