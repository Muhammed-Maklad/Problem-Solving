
nums1 = [1, 2, 3, 4]
nums2 = [2, 10, 20, 19]
k1 = 0
k2 = 0

k = k1 + k2
arr = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]

if k >= sum(arr):
    print(0)
else:
    left = 0
    right = max(arr)

    while left < right:
        mid = (left + right) // 2
        operations = sum(max(0, diff - mid) for diff in arr)

        if operations <= k:
            right = mid
        else:
            left = mid + 1

    level = left
    operations = sum(max(0, diff - level) for diff in arr)

    remaining = k - operations

    for i in range(len(arr)):
        arr[i] = min(arr[i], level)

    arr.sort(reverse=True)

    for i in range(remaining):
        if arr[i] > 0:
            arr[i] -= 1

    total = sum(diff ** 2 for diff in arr)
    print(total)
