class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        result = []
        for i in range(len(l)):
            subarray = nums[l[i]:r[i]+1]
            subarray = sorted(subarray)
            sub_res = []
            for x in range(1,len(subarray)):
                sub_res.append(subarray[x] - subarray[x-1])

            result.append(True if len(set(sub_res)) <= 1 else False)

        return result