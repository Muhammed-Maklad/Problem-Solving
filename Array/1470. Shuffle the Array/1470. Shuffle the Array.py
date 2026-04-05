class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res =[]
        for x in range(n):
            res.append(nums[x])
            res.append(nums[x+n])

        return res
    
    