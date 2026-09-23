class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """

        total = sum(nums)

        if x > total:
            return -1

        if x == total:
            return len(nums)

        k = total - x
        res = 0
        current_sum = 0
        left = 0

        for right, num in enumerate(nums):
            current_sum += num

            while current_sum > k:
                current_sum -= nums[left]
                left += 1

            if current_sum == k:
                res = max(res, right - left + 1)

        return -1 if res == 0 else len(nums) - res