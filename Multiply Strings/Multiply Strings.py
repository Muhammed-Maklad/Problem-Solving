class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
             return "0"

        m, n = len(num1), len(num2)
        arr = [0] * (m + n) 

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])      
                sum_ = mul + arr[i + j + 1]            
                arr[i + j + 1] = sum_ % 10           
                arr[i + j] += sum_ // 10           

        result = "".join(map(str, arr)).lstrip("0")
        return result if result else "0"
