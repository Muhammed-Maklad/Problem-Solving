class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for x in range(len(nums)):
            nums[x] = nums[x] % 2

        return(sorted(nums)) 