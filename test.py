hours = [0,1,2,3,4]
target = 2
total = sum(1 for x in hours if target <= x)
print(total)