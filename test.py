s = "(()(()))"

def scoreOfParentheses(s):
    stack = [0]

    for x in s:
        if x == "(":
            stack.append(0)
        else:
            value = stack.pop()

            if value == 0:
                value = 1
            else:
                value = 2 * value

            stack[-1] += value

    return stack[0]


print(scoreOfParentheses(s))