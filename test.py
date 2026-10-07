s = "()())()"

def valid(s):
    balance = 0

    for x in s:
        balance += (x == "(")

        if x == ")":
            if balance > 0:
                balance -= 1
            else:
                return False

    return balance == 0


def generate(current):
    res = []

    for i in range(len(current)):
        if current[i] == "(" or current[i] == ")":
            new_string = current[:i] + current[i + 1:]
            res.append(new_string)

    return res


result = [s]
visited = {s}
final = []

while result:

    next_level = []

    for current in result:

        if valid(current):
            final.append(current)

        else:
            for new_string in generate(current):

                if new_string not in visited:
                    visited.add(new_string)
                    next_level.append(new_string)

    if final:
        break

    result = next_level

print(final)