words = ["leetcode","win","loops","success"]
pref = "code"
total = 0
length = len(pref)
for word in words :
    if word[0:length] == pref:
        total += 1
print(total)
