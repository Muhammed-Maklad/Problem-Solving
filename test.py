nums = [1,2,5,2,3]
target = 2
nums = sorted(nums)

res = [i+1 for i , num in enumerate(nums) if num == target]

print(res)