class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def valid(s):
            balance = 0

            for x in s:
                if x == "(":
                    balance += 1

                elif x == ")":
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0


        result = [s]
        visited = {s}

        while result:

            final = []
            next_level = []

            for current in result:

                if valid(current):
                    final.append(current)
                    continue

                for i in range(len(current)):

                    if current[i] not in "()":
                        continue
                        
                    if i > 0 and current[i] == current[i - 1]:
                        continue

                    new_string = current[:i] + current[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_level.append(new_string)

            if final:
                return final

            result = next_level

        return [""]