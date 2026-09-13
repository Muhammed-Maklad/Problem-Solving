class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos , neg = 0 , 1
        res =  [0] * len(nums)

        for num in nums:
            if num > 0 :
                res[pos] = num
                pos += 2
            else:
                res[neg] = num 
                neg += 2
        return res