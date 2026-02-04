prices = [7,6,4,3,1]
ind = prices.index(min(prices))
print(ind)
prices = prices[ind : ]
print(max(prices)-prices[0])