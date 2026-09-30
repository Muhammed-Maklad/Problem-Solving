seq = "(()())"
Parentheses = 0
res = []

for x in seq:

    if x == "(":
        res.append(Parentheses % 2)
        Parentheses += 1

    else:
        Parentheses -= 1
        res.append(Parentheses % 2)

print(res)