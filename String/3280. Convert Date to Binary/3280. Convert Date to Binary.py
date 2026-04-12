class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        data = date.split("-")
        res = ""
        for x in range(len(data)) :
            num = bin(int(data[x]))[2:]
            res += num
            if x <  len(data) -1 :
                res += "-"
        
        return res