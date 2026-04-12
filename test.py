date = "2080-02-29" 
data = date.split("-")
res = ""
for x in range(len(data)) :
    num = bin(int(data[x]))[2:]
    res += num 
print(res)