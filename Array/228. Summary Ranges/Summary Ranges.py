
class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []

        arr = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                arr.append((start, nums[i-1]))
                start = nums[i]

        arr.append((start, nums[-1]))

        result = []
        for a, b in arr:
            if a == b:
                result.append(str(a))
            else:
                result.append(str(a) + "->" + str(b))

        return result
