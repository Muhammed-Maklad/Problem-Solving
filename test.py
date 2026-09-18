# nums = [1,2,3]
# res = [[]]

# for num in nums:
#     res.append([num])
# i = 0

# while i < len(nums):
#     j = i + 1
    
#     while j < len(nums):
#         subset = [nums[i]]
#         subset.append(nums[j])
#         res.append(subset)

#         j += 1

#     i += 1
# res.append(nums)
# print(res)

candies = [2,3,5,1,3]
extraCandies = 3
MaxCh= max(candies)
res = [True if x + extraCandies >= MaxCh else False for x in candies]

print(res)