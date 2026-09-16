costs = [1,6,3,1,2,5]
coins = 20
num = 0
costs.sort()
for cost in costs:
    if cost > coins:
        break
    num += 1
    coins -= cost
print(num)
