class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        j = i+1
        n = len(nums)
        cost = (nums[0] ) +(nums[i]) + (nums[j])

        while i < n:
            while j < n:
                if (nums[0] ) +(nums[i]) + (nums[j]) < cost :
                    cost = (nums[0] ) +(nums[i]) + (nums[j])
                
                j = j + 1
            i=i+1
            j = i+1    
        return cost