class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = []
        for x in range(len(A)):
            common = set(A[0:x+1]) & set(B[0:x+1])
            res.append(len(common))
        return res