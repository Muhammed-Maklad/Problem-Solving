nums = [3,1,-2,-5,2,-4]
pos , neg = 0 , 1
res =  [0] * len(nums)

for num in nums:
    if num > 0 :
        res[pos] = num
        pos += 2
    else:
        res[neg] = num 
        neg += 2

print(res)