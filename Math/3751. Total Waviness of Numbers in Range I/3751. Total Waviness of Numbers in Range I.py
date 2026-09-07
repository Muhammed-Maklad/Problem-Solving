class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
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
        return total
