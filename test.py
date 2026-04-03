test = ["X++","++X","--X","X--"]
res = 0 
for x in test:
    if "-" in x:
        res -= 1
    else:
        res += 1

print(res)