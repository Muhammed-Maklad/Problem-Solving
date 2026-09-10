nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]
result = []
for i in range(len(l)):
    subarray = nums[l[i]:r[i]+1]
    subarray = sorted(subarray)
    sub_res = []
    for x in range(1,len(subarray)):
        sub_res.append(subarray[x] - subarray[x-1])

    result.append(True if len(set(sub_res)) <= 1 else False)

print(result)