nums = [5,1]
minnum = min(nums)
maxnum = max(nums)

res = [ x for x in range(minnum,maxnum) if x not in nums]
print(res)