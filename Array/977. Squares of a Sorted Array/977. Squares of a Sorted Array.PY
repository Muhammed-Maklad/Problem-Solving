class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [x**2 for x in nums]
        nums.sort()
        return nums