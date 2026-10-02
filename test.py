n = 1
open, close = 0, 0
current = ""
results = []

def generate(n, open, close, current):
    if open == n and close == n:
        results.append(current)

    if open < n :
        generate(n, open + 1, close, current + "(")

    if close < open :
        generate(n, open, close + 1, current + ")")


generate(n, open, close, current)
print(results)