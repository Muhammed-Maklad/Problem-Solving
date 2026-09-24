class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for index, num in enumerate(nums):
        #     if index == sum(int(x) for x in str(num)):
        #         return index

        # return -1

        for index , num in enumerate(nums):
            total = 0
            while num :
                total += num % 10
                num /= 10
            if total == index :
                return index
        return -1 