class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        res = []

        for word in words:
            total = 0
            for char in word:
                total += weights[ord(char) - ord('a')]
            rem_total =   (total % 26)
            index  =  chr(ord('z') - rem_total)  
            res.append(index)
        return ''.join(res)