class Solution(object):
    def minSwaps(self, nums):
        total = 0
        visited = [False] * len(nums)

        arr = sorted(
            (sum(map(int, str(n))), n, i)
            for i, n in enumerate(nums)
        )

        for i in range(len(nums)):
            if visited[i] or arr[i][2] == i:
                continue

            j = i
            swaps = 0

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                swaps += 1

            total += swaps - 1

        return total