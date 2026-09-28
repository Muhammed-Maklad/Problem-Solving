s = "(1)+((2))+(((3)))"

level = 0
maxLevel = 0

for x in s:
    level += (x == "(") - (x == ")")
    maxLevel = max(maxLevel, level)
print(maxLevel)