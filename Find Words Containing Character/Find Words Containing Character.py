class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        res = []
        for word in range(len(words)):
            if x in words[word]:
                res.append(word)
        return res