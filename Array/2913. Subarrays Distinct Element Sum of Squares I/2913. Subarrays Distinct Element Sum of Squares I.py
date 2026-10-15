class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        size = len(nums)
        x  = 0 

        for x in range(size):
            seen = set()
            for j in range(x, size):
                seen.add(nums[j])
                count = len(seen)

                total += count * count

        return total