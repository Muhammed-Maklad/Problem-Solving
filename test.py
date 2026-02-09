arr = [1, 2, 3, 4]
n = len(arr)

result = [1] * n

for x in range(1,n):
    result[x] = arr[x-1] * result[x-1]

right_pointer = arr[-1]
for y in range(n-2,-1,-1):
    result[y] *= right_pointer
    right_pointer *= arr[y]

print(result)