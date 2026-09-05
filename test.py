A = [1,3,2,4]
B = [3,1,2,4]
res = []
for x in range(len(A)):
    common = set(A[0:x+1]) & set(B[0:x+1])
    res.append(len(common))

print(res)