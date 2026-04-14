class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        newVO , OldVO , new , Old= 0 ,0,0,0
        vowel = ["a","e","o","i","u"]

        for x in range(len(s)):
            if s[x] in vowel :
                newVO = s.count(s[x])
                OldVO = max(newVO, OldVO)
            else:
                new = s.count(s[x])
                Old = max(Old,new)
        
        return OldVO+Old