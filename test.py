res = 0

word = "hello"
pointer = 1

for x in range(len(word)-1):
    res += abs(ord(word[x])- ord(word[pointer]))
    pointer += 1


print(res)