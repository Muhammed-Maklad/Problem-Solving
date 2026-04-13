nums = [10,4,8,3] 
left = [0] * len(nums)
right = [0] * len(nums)
res = [0] * len(nums)

for i in range (1,len(nums)):
    left[i] = left[i-1] + nums[i-1]

for i in range (len(nums)-2 ,-1, -1):
    right[i] = right[i+1] + nums[i+1]

for i in range (len(nums)):
    res[i] = abs(left[i] - right[i])

print(left)
print(right)
print(res)