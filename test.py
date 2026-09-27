s = "(ed(et(oc))el)"

stack = []

for x in s:

    if x == "(":
        current = ""
        stack.append(current)

    elif x == ")":
        previous = stack.pop()
        current = current[::-1]
        current = current+previous

    else:
        current += x