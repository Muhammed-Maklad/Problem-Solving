class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mid = len(nums) // 2
        new = sorted ([x**2 for x  in nums])
        return (sum(new[mid:]) - sum(new[:mid]))