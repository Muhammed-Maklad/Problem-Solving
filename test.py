newVO , OldVO , new , Old= 0 ,0,0,0
vowel = ["a","e","o","i","u"]

s = "aeiaeia"
for x in range(len(s)):
    if s[x] in vowel :
        newVO = s.count(s[x])
        OldVO = max(newVO, OldVO)
    else:
        new = s.count(s[x])
        Old = max(Old,new)

print(OldVO+Old)