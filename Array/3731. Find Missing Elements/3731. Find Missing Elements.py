class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        minnum = min(nums)
        maxnum = max(nums)
        s = set(nums)
        res = [ x for x in range(minnum,maxnum) if x not in s]
        return res