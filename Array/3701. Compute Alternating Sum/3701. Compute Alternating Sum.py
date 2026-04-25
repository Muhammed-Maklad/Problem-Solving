class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(x if i % 2 == 0 else -x for i, x in enumerate(nums))
        return total 