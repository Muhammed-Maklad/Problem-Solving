words = ["abcd","def","xyz"]; weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]
index = 0 
res =""
for y in (words):
    total = 0
    for x in range(len(words[index])):
        postion = ord(y[x]) - ord('a')
        total += weights[postion]
    res += (chr(ord('a') + (25 - (total % 26))))
    index += 1
print(res)