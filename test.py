nums = [1, 2, 3, 1, 1, 3]

freq = {}
res = 0

for num in nums:
    if num in freq:
        res += freq[num]

    freq[num] = freq.get(num, 0) + 1

print(res)