nums = [1,3,5,7] 
total = 0

for x in range(0,len(nums),2):
    total += nums[x]

for x in range(1,len(nums),2):
    total -= nums[x]

print(total)