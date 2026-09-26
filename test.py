s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]
knowledge = dict(knowledge)

key = ""
current = ""
open = 0
while open < len(s):
    if s[open] == "(":
        close = s.find(")",open+1)
        key = (s[open+1:close])

        current +=  knowledge.get(key,"?")
        open = close+1

    else:
        current += s[open]
        open += 1

print(current)
