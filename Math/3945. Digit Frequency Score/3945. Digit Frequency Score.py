class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        return sum(map(int, n))
        # n = str(n)
        # data_list = list(n)
        # frequency = {}

        # for item in data_list:
        #     frequency[item] = frequency.get(item, 0) + 1

        # return sum(map(lambda x: int(x) * frequency[x], frequency))
