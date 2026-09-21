nums = [1,4,7,10,15]
k = 5
def check(nums, k):
    nums = set(nums)
    x = k
    while x in nums:
        x += k
    return x

print(check(nums,k))