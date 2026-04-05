nums = [2,5,1,3,4,7]
n = 3
arr1 = nums[0:n]
arr2 = nums[n:]
res =[]

for x in range(n):
    res.append(arr1[x])
    res.append(arr2[x])

print(res)