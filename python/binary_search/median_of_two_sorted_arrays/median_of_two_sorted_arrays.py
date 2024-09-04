class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        min_arr, max_arr = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        
        if min_arr == []:
            if len(max_arr) % 2 == 0:
                m = (len(max_arr) - 1) // 2
                return (max_arr[m] + max_arr[m + 1]) / 2
            else:
                m = (len(max_arr) - 1) // 2
                return (max_arr[m])

        lp = 0
        rp = len(min_arr) - 1
        total = len(min_arr) + len(max_arr)
        half = total // 2
        
        while lp <= rp:
            m = (lp + rp) // 2
            min_arr_left_partition = min_arr[:m + 1]
            spaces_left = half - len(min_arr_left_partition)
            max_arr_left_partition = max_arr[:spaces_left]

            if min_arr_left_partition[-1] > max_arr[spaces_left]:
                rp = m - 1
                continue
            elif max_arr_left_partition[-1] > min_arr[m + 1]:
                lp = m + 1
                continue

            if total % 2 == 0:
                end_of_left_partition = max(min_arr_left_partition[-1], max_arr_left_partition[-1])
                start_of_right_partition = min(min_arr[m + 1], max_arr[spaces_left])
                return (end_of_left_partition + start_of_right_partition) / 2
            else:
                start_of_right_partition = min(min_arr[m + 1], max_arr[spaces_left])
                return start_of_right_partition
        
        if total % 2 == 0:
            end_of_left_partition = max_arr[half - 1]
            if half == len(max_arr):
                start_of_right_partition = min_arr[0]
            else:
                start_of_right_partition = min(min_arr[0], max_arr[half])
            return (end_of_left_partition + start_of_right_partition) / 2
        else:
            start_of_right_partition = min(max_arr[half], min_arr[0])
            return start_of_right_partition
