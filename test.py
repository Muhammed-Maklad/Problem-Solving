start = 1
num = 10
res = []
non = []
for x in range(start, num+1):
    if x % 3 == 0 :
        non.append(x)
    else:
        res.append(x)

print(sum(res)- sum(non))