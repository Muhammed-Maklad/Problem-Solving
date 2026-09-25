# expression = "{a,{b,c}}"

# bracket = 0

# res = set()
# union = set()
# current = ""

# for x in expression:

#     if x == "{":
#         bracket += 1

#     elif x == "}":
#         if current:
#             union.add(current)
#             current = ""

#         bracket -= 1

#     if x.isalpha():
#         current += x

#     if x == "," and bracket == 1:
#         union.add(current)
#         current = ""


# def concatenate(A, B):
#     result = set()

#     for a in A:
#         for b in B:
#             result.add(a + b)

#     return result
# def parse(expression):

#     result = set()
#     current = ""

#     i = 0

#     while i < len(expression):

#         if expression[i].isalpha():
#             current += expression[i]

#         elif expression[i] == ",":
#             result.add(current)
#             current = ""

#         elif expression[i] == "{":

#             bracket = 1
#             j = i + 1

#             while bracket > 0:
#                 if expression[j] == "{":
#                     bracket += 1
#                 elif expression[j] == "}":
#                     bracket -= 1

#                 j += 1

#             inner_expression = expression[i + 1:j - 1]

#             inner_result = parse(inner_expression)

#             # لسه هنا محتاجين نقرر:
#             # Union ولا Concatenation؟

#         i += 1

#     if current:
#         result.add(current)

#     return result



num = 123
step  = 0

while num:
    if num % 2 == 0 :
        step +=1 
        num /= 2 
    else:
        step +=1 
        num -= 1
print(step)