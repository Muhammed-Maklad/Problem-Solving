s = "race a car"
res = ""
for alpha in s :
    if alpha.isalpha() :
        res += alpha.lower()

print(res == res [::-1])