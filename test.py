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

s = "abc"
indices = [0,1,2]
newS = [0]*len(s)

for i in range(len(s)):
    newS[indices[i]] = s[i]

print(''.join(i for i in newS))