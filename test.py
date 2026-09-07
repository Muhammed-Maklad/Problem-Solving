
num1 = 4848
num2 = 4848
total = 0

for number in range(num1, num2 + 1):

    length = len(str(number))

    if length < 3:
        continue

    x = 1

    while x < length - 1:

        if (str(number)[x] > str(number)[x + 1] and str(number)[x] > str(number)[x - 1]) or \
           (str(number)[x] < str(number)[x + 1] and str(number)[x] < str(number)[x - 1]):

            total += 1

        x += 1

print(total)

