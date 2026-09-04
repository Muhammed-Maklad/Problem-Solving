class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res =[]
        for num in reversed(nums):
            while num > 0:
                res.append(num % 10)
                num //= 10
        return res[::-1]