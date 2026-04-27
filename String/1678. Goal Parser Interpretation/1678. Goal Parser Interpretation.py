class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        result = ""
        for x in range (len(command)):
            if command[x] == "G":
                result += "G"
            elif command[x:x+2] == "()" :
                result += "o"
            elif command[x:x+4] == "(al)" :
                result += "al"
            else:
                pass
        return result