nums = [1,34,7]
digit = 9
digit = str(digit)
result = 0

for num in nums:
    result += str(num).count(digit)

print(result)