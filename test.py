strs = ["",""]

dic = []
for x in strs:
    dic.append(tuple(sorted(x)))

result = {}

for i, value in enumerate(dic):
    if value not in result:
        result[value] = []
    result[value].append(strs[i])

print(list(result.values()))

