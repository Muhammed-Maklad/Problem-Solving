cost = [1,2,3]
cost.sort(reverse=True)
total = 0
for x in range(1,len(cost)):
    if x % 3 != 2:

     total += cost[x]

print(total)