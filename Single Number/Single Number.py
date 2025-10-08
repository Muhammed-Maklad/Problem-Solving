class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res ^= n
        return res
    
s = Solution()
print(s.singleNumber([4,1,2,1,2]))  