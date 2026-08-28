nums =  [3,6,9]
steps = 0
for x in nums :
    if x % 3 == 0:
        steps += 0
    else:
        mod = x % 3
        steps += min(abs(x-mod), x+3)

print(steps)