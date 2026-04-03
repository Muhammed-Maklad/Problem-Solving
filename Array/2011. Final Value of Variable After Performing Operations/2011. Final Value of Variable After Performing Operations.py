class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = 0 
        for x in operations:
            if "-" in x:
                res -= 1
            else:
                res += 1

        return res