s = ")("
open = 0
add = 0
for x in s :
    if x=="(" :
        open += 1
    else:
        if open > 0 :
            open -= 1
        else :
            add += 1 


print(open + add)