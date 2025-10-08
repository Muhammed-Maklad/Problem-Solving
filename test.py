nums = [4,1]
set_nums = set(nums)

res = {x: nums.count(x) for x in set_nums}  
print([v for v in res.values() if v == 1][0])

