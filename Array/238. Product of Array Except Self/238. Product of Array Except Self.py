class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        result = [1] * n

        for x in range(1,n):
            result[x] = nums[x-1] * result[x-1]

        right_pointer = nums[-1]
        for y in range(n-2,-1,-1):
            result[y] *= right_pointer
            right_pointer *= nums[y]

        return result