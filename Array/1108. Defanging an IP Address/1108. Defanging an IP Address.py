class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        res = "".join("[.]" if x == "." else x for x in address)
        return (res)
    