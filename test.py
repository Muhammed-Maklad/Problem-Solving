x = 120
num = str(x)[::-1] if abs(x) == x else "-" + str(x)[:0:-1]
print(int(num))