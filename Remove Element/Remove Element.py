# Problem link: https://leetcode.com/problems/remove-element/
# Difficulty : Easy
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # Pointer for the position of the next non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

s = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(s.removeElement(nums, val)) 