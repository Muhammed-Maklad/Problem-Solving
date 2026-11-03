class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # max_num = max(nums)
        # total = sum(max_num - x for x in nums)

        # return total


        return max(nums) * len(nums) - sum(nums)