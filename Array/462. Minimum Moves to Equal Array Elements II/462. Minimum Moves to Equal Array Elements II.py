class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        if len(nums) == 1 :
            return 0
        
        nums.sort()
        mid = nums[len(nums)//2]
        res = 0
        for i in nums:
            res += abs(i-mid)
        return res