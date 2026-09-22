class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        res = 0

        for num in nums:
            if num in freq:
                res += freq[num]

            freq[num] = freq.get(num, 0) + 1
        return res