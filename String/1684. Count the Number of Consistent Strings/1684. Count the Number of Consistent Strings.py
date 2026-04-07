class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0 
        allow = set(allowed)
        for word in words :
            if set(word) <= allow:
                count += 1
            
        return count 