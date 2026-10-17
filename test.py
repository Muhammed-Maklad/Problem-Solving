nums = [37, 100]

sum_arr = [sum(int(x) for x in str(num)) for num in nums]

sorted_arr = sorted(nums, key=lambda num: (sum(int(x) for x in str(num)), num))

total = 0
for i in range(len(nums)):
    if nums[i] != sorted_arr[i]:
        j = nums.index(sorted_arr[i])
        nums[i], nums[j] = nums[j], nums[i]
        total += 1

print(total)