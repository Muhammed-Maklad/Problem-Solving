class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            sorted_left = merge_sort(left_half)
            sorted_right = merge_sort(right_half)

            return merge(sorted_left, sorted_right)

        def merge(left, right):
            merged_list = []
            i = 0 
            j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged_list.append(left[i])
                    i += 1
                else:
                    merged_list.append(right[j])
                    j += 1

           
            while i < len(left):
                merged_list.append(left[i])
                i += 1

            while j < len(right):
                merged_list.append(right[j])
                j += 1

            return merged_list

      
        merged_list = merge_sort(nums1 + nums2)
        n = len(merged_list)

        
        if n % 2 == 1:
            return float(merged_list[n // 2])
        else:
            mid1 = n // 2 - 1
            mid2 = n // 2
            return (float(merged_list[mid1]) + float(merged_list[mid2])) / 2.0
