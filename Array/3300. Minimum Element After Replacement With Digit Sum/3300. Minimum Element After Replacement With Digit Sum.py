class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in range(len(nums)):
            nums[x] = sum(int(d) for d in str(nums[x]))
        return min(nums)