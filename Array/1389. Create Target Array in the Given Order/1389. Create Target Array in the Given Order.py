class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        n = []
        for x , y in zip(nums,index):
            n[y:y] = [x]
        return n