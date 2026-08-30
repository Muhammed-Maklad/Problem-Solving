n = 101
n = str(n)
data_list = list(n)
frequency = {}

for item in data_list:
    frequency[item] = frequency.get(item, 0) + 1

print(sum(map(lambda x: int(x) * frequency[x], frequency)))

# n = 101
# n = str(n)

# print(sum(map(int, n)))