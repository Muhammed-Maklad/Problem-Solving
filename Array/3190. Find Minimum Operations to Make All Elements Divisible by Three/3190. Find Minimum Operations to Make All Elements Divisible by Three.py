class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = sum(min(x % 3, 3 - x % 3) for x in nums)
        return steps