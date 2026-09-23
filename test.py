nums = [5,6,7,8,9]
x = 4
k = sum(nums) - x 
res = 0 
current_sum = 0 
left = 0
for right, num in enumerate(nums):

    current_sum += num

    while current_sum > k:
        current_sum -= nums[left]
        left += 1 
    if current_sum == k:
        res = max(res , right - left + 1)

print(-1 if res <= 0 else len(nums) - res)