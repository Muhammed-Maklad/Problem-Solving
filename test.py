nums = [10, 12, 13, 14]

for x in range(len(nums)):
    nums[x] = sum(int(d) for d in str(nums[x]))

print(nums)