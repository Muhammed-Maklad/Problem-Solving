nums = [1,2,3]
mid = len(nums) // 2
new = sorted ([x**2 for x  in nums])
print(sum(new[mid:]) - sum(new[:mid]))