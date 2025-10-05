words = ["abc","bcd","aaaa","cbc"]; x = "a"

res = []
for word in range(len(words)):
    if x in words[word]:
        res.append(word)

print(res)
