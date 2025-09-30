s = "a23aa"
new_s = ""
for x in range(len(s)):
    if s[x].isdigit():
        new_s += s[x]
    else:
        break

print(0 if len(new_s) == 0 else new_s) 