class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        
        sign = 1 
        if s[0] == "-":
            sign =-1
            s = s[1:]
        elif s[0] == "+" :
            sign =1
            s = s[1:]
        new_s = ""
        for x in range(len(s)):
            if s[x].isdigit():
                new_s += s[x]
            else:
                break
        return 0 if len(new_s) == 0 else max(-2**31, min(int(new_s)*sign, 2**31 - 1))
    
s = Solution()

print (s.myAtoi("words and 987"))


