nums = [13,25,83,77]
res =[]
for num in reversed(nums):
    while num > 0:
        res.append(num % 10)
        num //= 10
print(res[::-1])