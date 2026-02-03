l1 = [2,4,3]
l2 = [5,6,4]

Fnum = ''.join(str(item) for item in l1[::-1])
Snum = ''.join(str(item) for item in l2[::-1])


print(Fnum)
print(Snum)
Total = int(Fnum)+int(Snum)

print(list(str(Total))[::-1])