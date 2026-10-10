
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        n = len(nums1)

        max_diff = 0
        diffs = [0] * n

        for i in range(n):
            d = abs(nums1[i] - nums2[i])
            diffs[i] = d

            if d > max_diff:
                max_diff = d

        if max_diff == 0 or k == 0:
            return sum(d * d for d in diffs)

        count = [0] * (max_diff + 1)

        for d in diffs:
            count[d] += 1

        for d in range(max_diff, 0, -1):
            if count[d] == 0:
                continue

            if k >= count[d]:
                k -= count[d]
                count[d - 1] += count[d]
                count[d] = 0
            else:
                count[d - 1] += k
                count[d] -= k
                k = 0
                break

        ans = 0

        for d in range(1, max_diff + 1):
            ans += count[d] * d * d

        return ans
