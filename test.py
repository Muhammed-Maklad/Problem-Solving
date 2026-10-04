s = "(*))"

def checkValidString(s):
    stack = []
    star = []

    for x in range(len(s)):

        if s[x] == "(":
            stack.append(x)

        elif s[x] == ")":
            if stack:
                stack.pop()
            elif star:
                star.pop()
            else:
                return False

        else:
            star.append(x)

    while stack and star:
        if stack[-1] < star[-1]:
            stack.pop()
            star.pop()
        else:
            return False

    return len(stack) == 0


print(checkValidString(s))