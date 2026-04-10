# char = 'z'
# result = 26 - (ord(char) % 97) 
# print(result)
s =  "abc"
index , res = 1 , 0
for char in s:
    Assci = 26 - (ord(char) % 97) 
    res += Assci*index
    index+=1

print(res)