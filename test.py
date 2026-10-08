s = "(()())(())"
res = ""
depth = 0

for x in s:
    if x == "(":
        if depth > 0:
            res += x
        depth += 1
    else:
        depth -= 1
        if depth > 0:
            res += x

print(res)