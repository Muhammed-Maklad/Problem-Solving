nums = [1,1]
total = 0
size = len(nums)
x  = 0 

for x in range(size):
    seen = set()
    for j in range(x, size):
        seen.add(nums[j])
        count = len(seen)

        total += count * count

print(total)