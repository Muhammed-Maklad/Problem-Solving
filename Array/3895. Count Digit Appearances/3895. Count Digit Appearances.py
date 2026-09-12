class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        digit = str(digit)
        result = 0

        for num in nums:
            result += str(num).count(digit)

        return result