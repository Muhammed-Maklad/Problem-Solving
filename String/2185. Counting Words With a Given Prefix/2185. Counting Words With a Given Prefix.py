class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        total = 0
        length = len(pref)
        for word in words :
            if word[0:length] == pref:
                total += 1
        return total